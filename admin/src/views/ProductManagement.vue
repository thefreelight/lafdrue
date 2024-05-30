<template>
  <div class="product-management">
    <div class="mb-4">
      <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          @click="showAddModal = true"
      >
        添加商品
      </button>
    </div>
    <SearchComponent :fields="searchFields" :filters="filters" @search="handleSearch"/>
    <ListTable :headers="headers" :items="products">
      <template v-slot:category="{ item }">
        {{ item.category.name }}
      </template>
      <template v-slot:status="{ item }">
        {{ item.status ? "激活" : "未激活" }}
      </template>
      <template v-slot:actions="{ item }">
        <button @click="editProduct(item)" class="text-indigo-600 hover:text-indigo-900">
          编辑
        </button>
        <button @click="openDeleteConfirmation(item.id)" class="text-red-600 hover:text-red-900 ml-4">
          删除
        </button>
      </template>
    </ListTable>
    <Pagination
        :current-page="currentPage"
        :total-pages="totalPages"
        @page-changed="handlePageChange"
    />
    <FormModal
        v-if="showAddModal || showEditModal"
        :title="showAddModal ? '添加商品' : '编辑商品'"
        :inputs="formInputs"
        :model="showAddModal ? newProduct : currentProduct"
        :onSave="showAddModal ? addProduct : saveProduct"
        :onClose="closeModal"
    />
    <DeleteConfirmationModal
        v-if="showDeleteConfirmation"
        :showModal="showDeleteConfirmation"
        title="删除商品"
        message="您确定要删除这个商品吗？此操作不能撤销。"
        :action="deleteProduct"
        @update:showModal="showDeleteConfirmation = $event"
    />
  </div>
</template>

<script setup>
import {ref, reactive, onMounted, watch, computed} from 'vue';
import axios from '../axios';
import ListTable from '../components/common/ListTable.vue';
import Pagination from '../components/common/Pagination.vue';
import FormModal from '../components/modals/FormModal.vue';
import SearchComponent from '../components/common/SearchComponent.vue';
import DeleteConfirmationModal from '../components/modals/DeleteConfirmationModal.vue';

const products = ref([]);
const currentProduct = ref({});
const newProduct = reactive({
  name: '',
  brand: '',
  category_id: null,
  price: null,
  status: 'active',
  // 确保所有的 formInputs 模型都有初始值
});
const showEditModal = ref(false);
const showAddModal = ref(false);
const showDeleteConfirmation = ref(false);
const currentPage = ref(1);
const totalPages = ref(0);
const pageSize = ref(10);
const categoriesForSearch = ref([{ value: null, text: '所有分类' }]);
const categoriesForForm = ref([]);   // 用于表单的分类数组，不包含“所有分类”
const selectedProductId = ref(null);


const headers = [
  {text: 'ID', value: 'id'},
  {text: '名称', value: 'name'},
  {text: '品牌', value: 'brand'},
  {text: '分类', value: 'category'},
  {text: '价格', value: 'price'},
  {text: '库存', value: 'stock'},
  {text: '状态', value: 'status'},
  {text: '操作', value: 'actions'},
];

const formInputs = computed(() => [
  {
    label: '名称',
    model: 'name',
    type: 'text',
    placeholder: '请输入商品名称',
    required: true,
  },
  {
    label: '品牌',
    model: 'brand',
    type: 'text',
    placeholder: '请输入商品品牌',
    required: true,
  },
  {
    label: '分类',
    model: 'category_id',
    type: 'select',
    options: categoriesForForm.value, // categoriesOptions 需要是一个包含分类信息的数组，格式为 [{ value: '分类ID', text: '分类名称' }]
    placeholder: '请选择商品分类',
    required: true,
  },
  {
    label: '价格',
    model: 'price',
    type: 'number',
    min: 0,
    placeholder: '请输入商品价格',
    required: true,
  },
  {
    label: '状态',
    model: 'status',
    type: 'select',
    options: [
      {value: 'active', text: '激活'},
      {value: 'inactive', text: '未激活'}
    ],
    placeholder: '请选择商品状态',
    required: true,
  }
]);


const searchFields = ref([
  // 定义搜索字段
  {
    label: '分类',
    model: 'category_id',
    type: 'select',
    options: categoriesForSearch.value,
    placeholder: '请选择分类'
  },
  {
    label: '名称',
    model: 'name',
    type: 'text',
    placeholder: '请输入商品名称'
  },
  {
    label: '状态',
    model: 'status',
    type: 'select',
    options: [
      {value: '', text: '所有状态'},
      {value: 'active', text: '激活'},
      {value: 'inactive', text: '未激活'}
    ],
    placeholder: '请选择状态'
  }
]);

//搜索条件配置
const filters = reactive({
  category_id: null,
  name: '',
  status: '',
});

// 获取分类数据的函数
async function fetchCategoriesData() {
  try {
    const response = await axios.get('/api/v1/categories/');
    const categoriesFromApi = response.data.items.map(category => ({
      value: category.id,
      text: category.name
    }));

    // 为搜索框添加“所有分类”选项
    categoriesForSearch.value = [{ value:'', text: '所有分类' }, ...categoriesFromApi];


    // 表单用的分类数组不包含“所有分类”
    categoriesForForm.value = [...categoriesFromApi];

    // 更新搜索字段中的分类选项
    const categorySearchField = searchFields.value.find(field => field.model === 'category_id');
    if (categorySearchField) {
      categorySearchField.options = categoriesForSearch.value;
    }

    // 如果是添加商品的情况，设置默认选中第一个实际的分类
    if (!currentProduct.value.id && categoriesForForm.value.length > 0) {
      newProduct.category_id = categoriesForForm.value[0].value;
    }


    // 更新filters以反映默认的“所有分类”选项
    filters.category_id = null;
  } catch (error) {
    console.error('Fetching categories failed:', error);
  }
}

// 在组件挂载时调用
onMounted(() => {
  fetchCategoriesData();
  fetchProducts()
});



// 假设的响应式变量，用于存储筛选条件
const params = computed(() => ({
  ...filters,
  page: currentPage.value,
  size: pageSize.value
}));

const fetchProducts = async () => {
  try {
    // 创建一个新的对象，只包含非空的筛选条件
    const validParams = Object.entries(params.value).reduce((acc, [key, value]) => {
      if (value !== '') {
        acc[key] = value;
      }
      return acc;
    }, {});

    // 发送GET请求到商品的API端点
    const response = await axios.get('/api/v1/products/', {
      params: validParams // 使用经过过滤的参数进行请求
    });

    // 更新商品列表和总页数
    products.value = response.data.items;
    totalPages.value = response.data.pages;
  } catch (error) {
    console.error('获取商品信息出错:', error);
  }
};

//查询功能
const handleSearch = (searchQuery) => {

  Object.assign(filters, searchQuery);
  // 重置当前页面为第一页，因为新的搜索可能有不同的分页数据
  currentPage.value = 1;

  fetchProducts(); // 调用 fetchUsers 函数，并传入新的搜索条件
};

const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchProducts();
};

watch(currentPage, fetchProducts); // This watcher will call fetchUsers whenever currentPage changes

// 添加商品的方法
const addProduct = async (productData) => {
  try {
    const response = await axios.post('/api/v1/products/', productData);
    if (response.status === 200) {
      // 如果添加成功，执行后续操作，例如关闭模态框，刷新商品列表
      showAddModal.value = false;
      fetchProducts(); // 假设这是一个获取商品列表的方法
    }
  } catch (error) {
    // 处理添加商品时的错误
    console.error('Error adding product:', error);
  }
};

// 保存商品的方法，用于编辑现有商品
const saveProduct = async (productData) => {
  try {
    const response = await axios.put(`/api/v1/products/${productData.id}`, productData);
    if (response.status === 200) {
      // 如果更新成功，执行后续操作
      showEditModal.value = false;
      fetchProducts(); // 刷新商品列表
    }
  } catch (error) {
    // 处理更新商品时的错误
    console.error('Error saving product:', error);
  }
};

// 编辑商品的方法
const editProduct = async (product) => {
  // 首先确保分类数据已加载
  if (categoriesForForm.value.length === 0) {
    await fetchCategoriesData();
  }

  // 然后设置当前商品数据
  currentProduct.value = { ...product };

  // 如果商品的category_id为空，但category对象存在并有id，则使用category的id
  if (!currentProduct.value.category_id && product.category && product.category.id) {
    currentProduct.value.category_id = product.category.id;
  }

  // 显示编辑模态框
  showEditModal.value = true;
};




// 打开删除确认模态框
const openDeleteConfirmation = (id) => {
  selectedProductId.value = id;
  showDeleteConfirmation.value = true;
};

// 删除商品的方法
const deleteProduct = async () => {
  if (selectedProductId.value === null || selectedProductId.value === undefined) {
    console.error('No product selected for deletion');
    return;
  }

  try {
    await axios.delete(`/api/v1/products/${selectedProductId.value}`);
    // 重新获取商品列表以更新界面
    fetchProducts();
    // 可能还需要关闭删除确认对话框或进行其他UI操作
  } catch (error) {
    console.error('Error deleting product:', error);
  }
};



// 在组件挂载时调用 fetchProducts 来加载第一页数据
onMounted(fetchProducts);


// 关闭模态框的方法
const closeModal = () => {
  showEditModal.value = false;
  showAddModal.value = false;
};

// 添加其他缺失的方法定义...

</script>

<style>
/* Add your styles here */
</style>
