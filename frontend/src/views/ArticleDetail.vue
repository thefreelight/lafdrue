<template>
  <div class="container mx-auto p-4">
    <div v-if="article" class="bg-gray-800 rounded-lg overflow-hidden border border-gray-700 shadow-lg p-6">
      <div class="flex items-center mb-4">
        <img :src="getAvatar(article.author)" alt="Author" class="w-10 h-10 rounded-full mr-4">
        <div>
          <span class="text-gray-400">{{ article.author || 'Unknown' }}</span>
          <n-tag type="success" class="ml-2">{{ getCategoryName(article.category_id) }}</n-tag>
          <div class="text-gray-500 text-sm">{{ formatDate(article.created_at) }}</div>
        </div>
      </div>
      <div v-if="article.image" class="mb-6">
        <img :src="article.image" alt="Article Image" class="w-full rounded-lg">
      </div>
      <div :class="{'p-6': article.image, 'p-6 w-full': !article.image}">
        <h2 class="text-2xl font-semibold mb-2 text-gray-100">{{ article.title }}</h2>
        <p class="text-gray-400 mb-4">{{ article.content }}</p>
      </div>
    </div>
    <div v-else class="text-gray-500 text-center text-xl mt-10">文章不存在</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from '../axios'
import { useMessage, NTag } from 'naive-ui'

const route = useRoute()
const article = ref(null)
const categories = ref([])
const message = useMessage()

const fetchArticle = async () => {
  try {
    const response = await axios.get(`/api/v1/articles/${route.params.id}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    article.value = response.data
  } catch (error) {
    message.error('获取文章失败')
  }
}

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/v1/article-categories/', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    categories.value = response.data.items
  } catch (error) {
    message.error('获取文章分类失败')
  }
}

const getCategoryName = (categoryId) => {
  const category = categories.value.find(c => c.id === categoryId)
  return category ? category.name : 'Unknown'
}

const getAvatar = (author) => {
  if (!author) {
    return 'https://via.placeholder.com/50'
  }
  return `https://ui-avatars.com/api/?name=${author}&background=random`
}

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}

onMounted(() => {
  fetchArticle()
  fetchCategories()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

.container {
  max-width: 800px;
}

.text-gray-400 {
  color: #a0aec0;
}

.text-gray-100 {
  color: #f7fafc;
}

.text-gray-500 {
  color: #718096;
}

.text-blue-400 {
  color: #63b3ed;
}

.font-custom {
  font-family: 'Great Vibes', cursive;
}
</style>
