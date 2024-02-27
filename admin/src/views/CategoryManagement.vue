<template>
  <div class="category-management">
    <div class="mb-4">
      <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          @click="showAddModal = true"
      >
        添加分类
      </button>
    </div>
    <SearchComponent :fields="searchFields" @search="handleSearch"/>
    <ListTable :headers="headers" :items="categories">
      <template v-slot:display="{ item }">
        {{ item.display ? '是' : '否' }}
      </template>
      <template v-slot:is_active="{ item }">
        {{ item.is_active ? '是' : '否' }}
      </template>
      <template v-slot:actions="{ item }">
        <button @click="editCategory(item)" class="text-indigo-600 hover:text-indigo-900">
          编辑
        </button>
        <button @click="openDeleteConfirmation(item.id)" class="text-red-600 hover:text-red-900 ml-4">
          删除
        </button>

      </template>
    </ListTable>



    <FormModal
        v-if="showEditModal"
        :title="'编辑分类'"
        :inputs="formInputs"
        :model="currentCategory"
        @save="saveCategory"
        @close="closeModal"
    />
    <FormModal
        v-if="showAddModal"
        :title="'添加分类'"
        :inputs="formInputs"
        :model="newCategory"
        @save="addCategory"
        @close="closeModal"
    />
  </div>

  <!-- 删除确认模态框 -->
  <DeleteConfirmationModal
      v-if="showDeleteConfirmation"
      :showModal="showDeleteConfirmation"
      title="删除分类"
      message="您确定要删除这个分类吗？此操作不能撤销。"
      :action="confirmDeleteCategory"
      @update:showModal="updateShowDeleteConfirmation"
  />

  <Pagination
    :current-page="currentPage"
    :total-pages="totalPages"
    @page-changed="handlePageChange"
/>

</template>

<script setup>
import ListTable from '../components/ListTable.vue';
import Pagination from '../components/Pagination.vue';
import FormModal from '../components/FormModal.vue';
import SearchComponent from '../components/SearchComponent.vue';
import DeleteConfirmationModal from '../components/DeleteConfirmationModal.vue';
import {ref, reactive, onMounted, watch} from 'vue';
import axios from '../axios';

const categories = ref([]);
const currentCategory = ref(null);
const showEditModal = ref(false);
const showAddModal = ref(false);
const currentPage = ref(1);
const totalPages = ref(0);
const pageSize = ref(10); // 假设您的API支持自定义每页显示的数量
const showDeleteConfirmation = ref(false); // 控制删除确认模态框的显示
const selectedCategoryId = ref(null); // 选中的分类ID

// 定义筛选条件的响应式对象
const filters = reactive({
  name: '', // 分类名称的筛选条件
  // 如果有其他筛选条件，也可以在这里添加
});

const searchFields = ref([
  {
    label: '分类名称',
    model: 'name',
    type: 'text', // 假设搜索字段是文本类型
    placeholder: '搜索分类名称...', // 输入框内的占位符文本
  },
  // 可以根据需要继续添加其他搜索字段
]);
const newCategory = reactive({name: '', is_active: true, display: true, order: 0});

const headers = [
  {text: 'ID', value: 'id'},
  {text: '分类名称', value: 'name'},
  {text: '是否激活', value: 'is_active'},
  {text: '是否显示', value: 'display'},
  {text: '排序', value: 'order'},
  {text: '操作', value: 'actions'},
];

const formInputs = [
  {label: '分类名称', model: 'name', type: 'text', required: true},
  {label: '是否激活', model: 'is_active', type: 'checkbox'},
  {label: '是否显示', model: 'display', type: 'checkbox'},
  {label: '排序', model: 'order', type: 'number'},
];




// 分页逻辑
const fetchCategories = async () => {
  try {
    // 创建一个新的对象，只包含非空的筛选条件
    const validParams = Object.entries(filters).reduce((acc, [key, value]) => {
      // 如果值不是空字符串，则包含此参数
      if (value !== '') {
        acc[key] = value;
      }
      return acc;
    }, {});

    // 添加分页参数
    validParams.page = currentPage.value;
    validParams.size = pageSize.value;

    const response = await axios.get('/api/v1/categories/', {
      params: validParams // 使用经过过滤的参数进行请求
    });

    // 假设后端返回的格式为 { items: [], totalPages: Number }
    categories.value = response.data.items;
    totalPages.value = response.data.pages;
  } catch (error) {
    console.error('Error fetching categories:', error);
  }
};


// 处理分页组件页码变更的函数
const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchCategories();
};

// 组件挂载时获取第一页数据
onMounted(() => {
  fetchCategories();
});

// 监听当前页变化
// 观察currentPage的变化，以便重新获取数据
watch(currentPage, fetchCategories);

// 监听筛选条件的变化
watch(filters, () => {
  currentPage.value = 1; // 重置到第一页
  fetchCategories();
});

const handleSearch = (searchQuery) => {
  // 例如，如果您的搜索字段是“name”，则更新筛选条件
  filters.name = searchQuery.name;
  // 重置当前页码为 1
  currentPage.value = 1;
  // 重新获取分类数据
  fetchCategories();
};


const addCategory = async (category) => {
  try {
    await axios.post('/api/v1/categories/', category);
    fetchCategories();
    showAddModal.value = false;
  } catch (error) {
    console.error('Error adding category:', error);
  }
};

const editCategory = (category) => {
  currentCategory.value = category;
  showEditModal.value = true;
};

const saveCategory = async (category) => {
  try {
    await axios.put(`/api/v1/categories/${category.id}`, category);
    fetchCategories();
    showEditModal.value = false;
  } catch (error) {
    console.error('Error saving category:', error);
  }
};


// 用户确认删除操作时调用的方法
// 在点击删除按钮时调用的方法，设置选中的分类ID并显示确认模态框
const openDeleteConfirmation = (categoryId) => {
  selectedCategoryId.value = categoryId;
  showDeleteConfirmation.value = true;
};

// 实际执行删除操作的函数
const deleteCategory = async (categoryId) => {
  try {
    // 确保传递的是一个有效的ID
    if (typeof categoryId === 'number') {
      await axios.delete(`/api/v1/categories/${categoryId}`);
      fetchCategories();
      showDeleteConfirmation.value = false;
    } else {
      console.error('Invalid category ID:', categoryId);
    }
  } catch (error) {
    console.error('Error deleting category:', error);
  }
};

// 用户确认删除操作时调用的方法
const confirmDeleteCategory = () => {
  if (selectedCategoryId.value !== null && typeof selectedCategoryId.value === 'number') {
    deleteCategory(selectedCategoryId.value);
  } else {
    console.error('No category selected or selected category ID is not a number.');
  }
};

// 更新删除确认模态框的显示状态
const updateShowDeleteConfirmation = (value) => {
  showDeleteConfirmation.value = value;
};

// 在点击删除按钮时调用的方法，设置选中的分类ID并显示确认模态框

const closeModal = () => {
  showEditModal.value = false;
  showAddModal.value = false;
};

onMounted(() => {
  fetchCategories();
});
</script>

<style>
/* Add your styles here */
</style>
