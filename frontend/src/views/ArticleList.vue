<template>
  <div class="container mx-auto p-4">
    <!-- Header Section -->
    <div class="bg-gradient-to-r from-green-400 to-blue-500 rounded-lg p-10 text-center text-4xl text-white font-semibold mb-10 font-custom">
      Do more useless things
    </div>

    <!-- Tags Section -->
    <div class="flex justify-center space-x-4 mb-10">
      <n-tag type="success" @click="filterCategory(null)">All</n-tag>
      <n-tag v-for="category in categories" :key="category.id" :type="getTagType(category.name)" @click="filterCategory(category.id)">
        {{ category.name }}
      </n-tag>
    </div>

    <!-- Articles Section -->
    <div v-if="filteredArticles.length === 0" class="text-gray-500 text-center text-xl mt-10">暂无文章</div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
          v-for="article in filteredArticles"
          :key="article.id"
          class="bg-gray-800 rounded-lg overflow-hidden border border-gray-700 shadow-lg p-6"
      >
        <div class="flex items-center mb-4">
          <img :src="getAvatar(article.author)" alt="Author" class="w-10 h-10 rounded-full mr-4">
          <div>
            <span class="text-gray-400">{{ article.author || 'Unknown' }}</span>
            <n-tag type="success" class="ml-2">{{ getCategoryName(article.category_id) }}</n-tag>
          </div>
        </div>
        <div :class="{'p-6': article.image, 'p-6 w-full': !article.image}">
          <h2 class="text-2xl font-semibold mb-2 text-gray-100">{{ article.title }}</h2>
          <p class="text-gray-400 mb-4">{{ article.content.substring(0, 100) }}...</p>
          <router-link :to="`/articles/${article.id}`" class="text-blue-400 hover:underline">
            阅读更多
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import { useMessage, NTag } from 'naive-ui'

const articles = ref([])
const filteredArticles = ref([])
const categories = ref([])
const selectedCategory = ref(null)
const message = useMessage()

const fetchArticles = async () => {
  try {
    const response = await axios.get('/api/v1/articles/', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    articles.value = response.data.items
    filterCategory(null)
  } catch (error) {
    message.error('获取文章列表失败')
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

const filterCategory = (categoryId) => {
  selectedCategory.value = categoryId
  if (categoryId === null) {
    filteredArticles.value = articles.value
  } else {
    filteredArticles.value = articles.value.filter(article => article.category_id === categoryId)
  }
}

const getCategoryName = (categoryId) => {
  const category = categories.value.find(c => c.id === categoryId)
  return category ? category.name : 'Unknown'
}

const getTagType = (categoryName) => {
  switch (categoryName) {
    case 'Genesis': return 'info'
    case '碎碎念': return 'warning'
    case 'Help': return 'primary'
    default: return 'default'
  }
}

// 生成默认头像的函数
const getAvatar = (author) => {
  if (!author) {
    return 'https://via.placeholder.com/50'  // 默认头像 URL
  }
  return `https://ui-avatars.com/api/?name=${author}&background=random`  // 使用 ui-avatars 生成头像
}

onMounted(() => {
  fetchArticles()
  fetchCategories()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

.container {
  max-width: 1200px;
}

.bg-gradient-to-r {
  background: linear-gradient(to right, #38b2ac, #4299e1);
}

.text-gray-400 {
  color: #a0aec0;
}

.text-gray-100 {
  color: #f7fafc;
}

.text-blue-400 {
  color: #63b3ed;
}

.font-custom {
  font-family: 'Great Vibes', cursive;
}
</style>
