<template>
  <div class="container mx-auto p-6">
    <n-button type="primary" @click="openCreateModal">新增文章</n-button>
    <n-table :columns="columns" :data="articles">
      <template #action="{ row }">
        <n-button size="small" type="primary" @click="editArticle(row)">编辑</n-button>
        <n-button size="small" type="error" @click="deleteArticle(row.id)">删除</n-button>
      </template>
    </n-table>

    <!-- Create/Edit Article Modal -->
    <n-modal v-model:show="showArticleModal" title="文章">
      <n-form :model="currentArticle" label-width="80px">
        <n-form-item label="标题" path="title">
          <n-input v-model:value="currentArticle.title" />
        </n-form-item>
        <n-form-item label="内容" path="content">
          <n-input v-model:value="currentArticle.content" type="textarea" />
        </n-form-item>
        <n-form-item label="作者" path="author">
          <n-input v-model:value="currentArticle.author" />
        </n-form-item>
        <n-form-item label="分类" path="category_id">
          <n-select v-model:value="currentArticle.category_id" :options="categoryOptions" />
        </n-form-item>
      </n-form>
      <template #footer>
        <n-button @click="showArticleModal = false">取消</n-button>
        <n-button type="primary" @click="saveArticle">保存</n-button>
      </template>
    </n-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import { useMessage } from 'naive-ui'

const showArticleModal = ref(false)
const articles = ref([])
const categories = ref([])
const currentArticle = ref({ title: '', content: '', author: '', category_id: null })

const message = useMessage()

const columns = [
  { title: 'ID', key: 'id' },
  { title: '标题', key: 'title' },
  { title: '内容', key: 'content' },
  { title: '作者', key: 'author' },
  { title: '分类', key: 'category_id' },
  { title: '操作', key: 'action' }
]

const categoryOptions = ref([])

const fetchArticles = async () => {
  try {
    const response = await axios.get('/api/v1/articles')
    articles.value = response.data.items
  } catch (error) {
    message.error('获取文章列表失败')
  }
}

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/v1/article-categories')
    categories.value = response.data.items
    categoryOptions.value = categories.value.map(category => ({ label: category.name, value: category.id }))
  } catch (error) {
    message.error('获取分类列表失败')
  }
}

const openCreateModal = () => {
  currentArticle.value = { title: '', content: '', author: '', category_id: null }
  showArticleModal.value = true
}

const editArticle = (article) => {
  currentArticle.value = { ...article }
  showArticleModal.value = true
}

const saveArticle = async () => {
  try {
    if (currentArticle.value.id) {
      await axios.put(`/api/v1/articles/${currentArticle.value.id}`, currentArticle.value)
      message.success('文章更新成功')
    } else {
      await axios.post('/api/v1/articles', currentArticle.value)
      message.success('文章创建成功')
    }
    showArticleModal.value = false
    fetchArticles()
  } catch (error) {
    message.error('文章保存失败')
  }
}

const deleteArticle = async (id) => {
  try {
    await axios.delete(`/api/v1/articles/${id}`)
    message.success('文章删除成功')
    fetchArticles()
  } catch (error) {
    message.error('文章删除失败')
  }
}

onMounted(() => {
  fetchArticles()
  fetchCategories()
})
</script>

<style scoped>
/* 添加样式 */
</style>
