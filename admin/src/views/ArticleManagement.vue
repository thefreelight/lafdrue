<template>
  <div class="container mx-auto p-6">
    <SearchComponent :fields="searchFields" @search="handleSearch" />
    <div class="flex justify-end mb-4 space-x-4 mt-4">
      <button @click="openCreateModal" class="bg-blue-500 text-white px-4 py-2 rounded">新增文章</button>
    </div>
    <ListTable :headers="articleHeaders" :items="articles">
      <template v-slot:author="{ item }">
        {{ item.author || '未知' }}
      </template>
      <template v-slot:category_id="{ item }">
        {{ getCategoryName(item.category_id) }}
      </template>
      <template v-slot:language="{ item }">
        {{ item.language || '未知' }}
      </template>
      <template v-slot:actions="{ item }">
        <button @click="editArticle(item)" class="text-indigo-600 hover:text-indigo-900 mr-4">
          编辑
        </button>
        <button @click="openDeleteConfirmation(item.id)" class="text-red-600 hover:text-red-900 ml-4">
          删除
        </button>
      </template>
    </ListTable>
    <AddArticle
        v-if="showEditArticleModal"
        :title="selectedArticle.id ? '编辑文章' : '新增文章'"
        :model="selectedArticle"
        :categories="categories"
        @onSave="handleSaveArticle"
        @onClose="handleCloseModal"
    />
    <DeleteConfirmationModal
        v-if="showDeleteConfirmation"
        :showModal="showDeleteConfirmation"
        title="删除文章"
        message="您确定要删除这篇文章吗？此操作不能撤销。"
        :action="deleteArticle"
        @update:showModal="showDeleteConfirmation = $event"
    />
    <Pagination
        :current-page="currentPage"
        :total-pages="totalPages"
        @page-changed="handlePageChange"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, reactive } from 'vue';
import axios from '../axios';
import ListTable from '../components/common/ListTable.vue';
import DeleteConfirmationModal from '../components/modals/DeleteConfirmationModal.vue';
import Pagination from '../components/common/Pagination.vue';
import SearchComponent from '../components/common/SearchComponent.vue';
import AddArticle from '../components/common/AddArticle.vue'; // 引入新增文章组件

const articles = ref([]);
const showEditArticleModal = ref(false);
const showDeleteConfirmation = ref(false);
const selectedArticle = ref({});
const selectedId = ref(null);
const currentPage = ref(1);
const totalPages = ref(0);
const pageSize = ref(10);
const categories = ref([]);

const articleHeaders = [
  { text: 'ID', value: 'id' },
  { text: '标题', value: 'title' },
  { text: '内容', value: 'content' },
  { text: '作者', value: 'author' },
  { text: '分类', value: 'category_id' },
  { text: '语言', value: 'language' },
  { text: '操作', value: 'actions' },
];

const searchFields = ref([
  { label: 'ID', model: 'id', type: 'text', placeholder: '搜索 ID...' },
  { label: '标题', model: 'title', type: 'text', placeholder: '搜索标题...' },
  { label: '作者', model: 'author', type: 'text', placeholder: '搜索作者...' },
  { label: '分类', model: 'category_id', type: 'select', options: categories.value, placeholder: '选择分类...' },
  { label: '语言', model: 'language', type: 'text', placeholder: '搜索语言...' }
]);

const filters = reactive({
  id: '',
  title: '',
  author: '',
  category_id: '',
  language: ''
});

const handleSearch = (searchQuery) => {
  Object.assign(filters, searchQuery);
  currentPage.value = 1;
  fetchArticles();
};

watch(categories, (newCategories) => {
  const categoryField = searchFields.value.find(field => field.model === 'category_id');
  if (categoryField) {
    categoryField.options = [
      ...newCategories.map(category => ({ value: category.id, text: category.name }))
    ];
  }
});

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/v1/article-categories');
    if (response.data && Array.isArray(response.data)) {
      categories.value = response.data.map(category => ({
        value: category.id,
        text: category.name
      }));
    }
  } catch (error) {
    console.error('获取分类失败:', error);
  }
};

onMounted(fetchCategories);

const handleSaveArticle = async (formData) => {
  try {
    if (formData.id) {
      await axios.put(`/api/v1/articles/${formData.id}`, formData);
    } else {
      await axios.post('/api/v1/articles', formData);
    }
    showEditArticleModal.value = false;
    fetchArticles();
  } catch (error) {
    console.error('保存文章失败:', error);
  }
};

const handleCloseModal = () => {
  showEditArticleModal.value = false;
};

const params = computed(() => ({
  ...filters,
  page: currentPage.value,
  size: pageSize.value
}));

const fetchArticles = async () => {
  try {
    const validParams = Object.entries(params.value).reduce((acc, [key, value]) => {
      if (value !== '') {
        acc[key] = value;
      }
      return acc;
    }, {});

    const response = await axios.get('/api/v1/articles', {
      params: validParams
    });
    articles.value = response.data.items;
    totalPages.value = Math.ceil(response.data.total / pageSize.value);
  } catch (error) {
    console.error('There was an error fetching the articles:', error);
  }
};

const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchArticles();
};

watch(filters, fetchArticles, { deep: true });
watch(currentPage, fetchArticles);

const deleteArticle = async () => {
  try {
    await axios.delete(`/api/v1/articles/${selectedId.value}`);
    showDeleteConfirmation.value = false;
    fetchArticles();
  } catch (error) {
    console.error('删除文章失败:', error);
  }
};

const editArticle = (article) => {
  selectedArticle.value = { ...article };
  showEditArticleModal.value = true;
};

const openDeleteConfirmation = (id) => {
  selectedId.value = id;
  showDeleteConfirmation.value = true;
};

const openCreateModal = () => {
  selectedArticle.value = { title: '', content: '', author: '', category_id: null, language: 'zh' };
  showEditArticleModal.value = true;
};

const getCategoryName = (categoryId) => {
  const category = categories.value.find(category => category.value === categoryId);
  return category ? category.text : '未知';
};

onMounted(fetchArticles);
</script>

<style scoped>
/* 可以在此处添加特定的CSS样式 */
</style>
