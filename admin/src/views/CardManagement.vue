<template>
  <div class="card-key-management">
    <div class="mb-4">
      <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          @click="showAddModal = true"
      >
        上传卡密
      </button>
    </div>
    <SearchComponent :fields="searchFields" :filters="filters" @search="handleSearch"/>
    <ListTable :headers="headers" :items="cardKeys">
      <template v-slot:category="{ item }">
        {{ item.product.category.name }}
      </template>
      <template v-slot:product="{ item }">
        {{ item.product.name }}
      </template>
      <template v-slot:is_used="{ item }">
        {{ item.is_used ? '已使用' : '未使用' }}
      </template>
      <template v-slot:actions="{ item }">
        <button @click="editCardKey(item)" class="text-indigo-600 hover:text-indigo-900">
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
    v-if="showAddModal"
    title="上传卡密"
    :inputs="formInputs"
    v-model="cardKeyForm"
    :onSave="addCardKey"
    :onClose="closeModal"
    :useVModel="true"
  />

  <FormModal
    v-if="showEditModal"
    title="编辑卡密"
    :inputs="formInputs"
    v-model="currentCardKey"
    :onSave="saveCardKey"
    :onClose="closeModal"
  />
    <DeleteConfirmationModal
        v-if="showDeleteConfirmation"
        :showModal="showDeleteConfirmation"
        title="删除卡密"
        message="您确定要删除这些卡密吗?此操作不能撤销。"
        :action="deleteCardKeys"
        @update:showModal="showDeleteConfirmation = $event"
    />
  </div>
</template>

<script setup>
import {ref, reactive, onMounted, watch, computed, nextTick} from 'vue';
import axios from '../axios';
import ListTable from '../components/ListTable.vue';
import Pagination from '../components/Pagination.vue';
import FormModal from '../components/FormModal.vue';
import SearchComponent from '../components/SearchComponent.vue';
import DeleteConfirmationModal from '../components/DeleteConfirmationModal.vue';

const cardKeys = ref([]);
const currentCardKey = ref({});
const cardKeyForm = reactive({
  code: '',
  category_id: null,
  product_id: null,
});
const showEditModal = ref(false);
const showAddModal = ref(false);
const showDeleteConfirmation = ref(false);
const currentPage = ref(1);
const totalPages = ref(0);
const pageSize = ref(10);
const categories = ref([]);
const productsByCategory = ref([]);
const selectedCardKeyIds = ref([]);


const headers = [
  {text: 'ID', value: 'id'},
  {text: '卡密代码', value: 'code'},
  {text: '商品分类', value: 'category'},
  {text: '商品', value: 'product'},
  {text: '是否已使用', value: 'is_used'},
  {text: '操作', value: 'actions'},
];

const searchFields = ref([
  {
    label: '卡密代码',
    model: 'code',
    type: 'text',
    placeholder: '请输入卡密代码',
  },
  {
    label: '是否已售出',
    model: 'is_used',
    type: 'select',
    options: [
      {value: '', text: '所有'},
      {value: 'true', text: '已售出'},
      {value: 'false', text: '未售出'},
    ],
    placeholder: '请选择使用状态',
  },
]);

const props = defineProps({
  // ...
  categories: Array,
  productsByCategory: Array,
});

const formInputs = computed(() => [
  {
    label: '卡密信息',
    model: 'code',
    type: 'textarea',  // 将类型改为 textarea
    placeholder: '请输入卡密信息,每行一个卡密',
    required: true,
  },
  {
    label: '请选择商品分类',
    model: 'category_id',
    type: 'select',
    options: categories.value,
    optionLabel: 'name',
    optionValue: 'id',
    placeholder: '请选择商品分类',
    required: true,
  },
  {
    label: '商品',
    model: 'product_id',
    type: 'select',
    options: productsByCategory.value,
    optionLabel: 'name',
    optionValue: 'id',
    placeholder: '请选择商品',
    required: true,
  },
]);

const filters = reactive({
  code: '',
  is_used: '',
});

// 根据选定的分类获取商品数据
const fetchProductsByCategory = async () => {
  if (!cardKeyForm.category_id) {
    productsByCategory.value = [];
    return;
  }

  try {
    const response = await axios.get('/api/v1/products/', {
      params: {
        category_id: cardKeyForm.category_id,
      },
    });
    productsByCategory.value = response.data.items;
  } catch (error) {
    console.error('Failed to fetch products by category:', error);
    productsByCategory.value = [];
  }
};
// 获取商品分类和商品数据的方法
const fetchData = async () => {
  await fetchCategories();
  if (categories.value.length > 0) {
    cardKeyForm.category_id = categories.value[0].id;
    await fetchProductsByCategory();
    if (productsByCategory.value.length > 0) {
      cardKeyForm.product_id = productsByCategory.value[0].id;
    }
  }
};

// 在组件挂载时调用 fetchData
onMounted(fetchData);

// 在组件挂载时调用 fetchData
onMounted(fetchData);

// 监听 cardKeyForm.category_id 的变化
watch(
  () => cardKeyForm.category_id,
  async (newCategoryId) => {
    if (newCategoryId) {
      await fetchProductsByCategory();
      if (productsByCategory.value.length > 0) {
        cardKeyForm.product_id = productsByCategory.value[0].id;
      } else {
        cardKeyForm.product_id = null;
      }
    } else {
      productsByCategory.value = [];
      cardKeyForm.product_id = null;
    }
  }
);


const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/v1/categories/');
    categories.value = response.data.items;
  } catch (error) {
    console.error('获取商品分类失败:', error);
  }
};



const params = computed(() => ({
  ...filters,
  page: currentPage.value,
  size: pageSize.value,
}));

const fetchCardKeys = async () => {
  try {
    const validParams = Object.entries(params.value).reduce((acc, [key, value]) => {
      if (value !== '') {
        acc[key] = value;
      }
      return acc;
    }, {});

    const response = await axios.get('/api/v1/card-keys/', {
      params: validParams,
    });

    cardKeys.value = response.data.items;
    totalPages.value = response.data.pages;
  } catch (error) {
    console.error('获取卡密失败:', error);
  }
};

const handleSearch = (searchQuery) => {
  Object.assign(filters, searchQuery);
  currentPage.value = 1;
  fetchCardKeys();
};

const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchCardKeys();
};

watch(currentPage, fetchCardKeys);

const addCardKey = async () => {
  try {
    const cardKeyCodes = cardKeyForm.code.split('\n').map((code) => code.trim());
    for (const code of cardKeyCodes) {
      if (code) {
        await axios.post('/api/v1/card-keys/', {
          code,
          product_id: cardKeyForm.product_id,
        });
      }
    }
    showAddModal.value = false;
    cardKeyForm.code = '';
    cardKeyForm.category_id = categories.value[0].id;
    cardKeyForm.product_id = productsByCategory.value[0].id;
    fetchCardKeys();
  } catch (error) {
    console.error('上传卡密失败:', error);
  }
};

const saveCardKey = async (cardKeyData) => {
  try {
    await axios.put(`/api/v1/card-keys/${cardKeyData.id}`, cardKeyData);
    showEditModal.value = false;
    fetchCardKeys();
  } catch (error) {
    console.error('保存卡密失败:', error);
  }
};

onMounted(() => {
  fetchCategories().then(() => {
    cardKeyForm.category_id = categories.value[0].id;
    fetchProductsByCategory().then(() => {
      cardKeyForm.product_id = productsByCategory.value[0].id;
    });
  });
  fetchCardKeys();
});

const editCardKey = (cardKey) => {
  currentCardKey.value = { ...cardKey };
  showEditModal.value = true;
};

const openDeleteConfirmation = (ids) => {
  selectedCardKeyIds.value = Array.isArray(ids) ? ids : [ids];
  showDeleteConfirmation.value = true;
};

const deleteCardKeys = async () => {
  try {
    for (const id of selectedCardKeyIds.value) {
      await axios.delete(`/api/v1/card-keys/${id}`);
    }
    fetchCardKeys();
  } catch (error) {
    console.error('删除卡密失败:', error);
  }
};

const closeModal = () => {
  showEditModal.value = false;
  showAddModal.value = false;
  cardKeyForm.value = {
    code: '',
    category_id: null,
    product_id: null,
  };
};

onMounted(() => {
  fetchCategories();
  fetchCardKeys();
});
</script>

<style>
/* Add your styles here */
</style>