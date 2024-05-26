<template>
  <div class="container mx-auto p-4">
    <!-- Header Section -->
    <div class="bg-gradient-to-r from-green-400 to-blue-500 rounded-lg p-10 text-center text-4xl text-white font-semibold mb-10 font-custom">
      Do more useless things
    </div>

    <!-- Tags Section -->
    <div class="flex justify-center space-x-4 mb-10">
      <button @click="fetchArticles(null)" class="bg-green-500 text-white px-4 py-2 rounded-full focus:outline-none">All</button>
      <button v-for="category in categories" :key="category.id" @click="fetchArticles(category.id)" :class="getTagClass(category.name)">
        {{ category.name }}
      </button>
    </div>

    <!-- Articles Section -->
    <div v-if="articles.length === 0" class="text-gray-500 text-center text-xl mt-10">暂无文章</div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
          v-for="article in articles"
          :key="article.id"
          class="bg-gray-800 rounded-lg overflow-hidden border border-gray-700 shadow-lg p-6"
      >
        <div class="flex items-center mb-4">
          <img :src="getAvatar(article.author)" alt="Author" class="w-10 h-10 rounded-full mr-4">
          <div>
            <span class="text-gray-400">{{ article.author || 'Unknown' }}</span>
            <span class="ml-2 bg-green-500 text-white px-2 py-1 rounded-full">{{ getCategoryName(article.category_id) }}</span>
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
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from '../axios'
import { useMessage } from 'naive-ui'

const articles = ref([])
const categories = ref([])
const message = useMessage()
const selectedLanguage = ref('en')  // 默认语言

const fetchArticles = async (categoryId) => {
  try {
    const response = await axios.get('/api/v1/articles/', {
      params: {
        category_id: categoryId,
        language: selectedLanguage.value
      },
      headers: {
        'Content-Type': 'application/json'
      }
    })
    articles.value = response.data.items
  } catch (error) {
    message.error('获取文章列表失败')
  }
}

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/v1/article-categories/', {
      params: {
        language: selectedLanguage.value
      },
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

const getTagClass = (categoryName) => {
  switch (categoryName) {
    case 'Genesis': return 'bg-blue-500 text-white px-4 py-2 rounded-full focus:outline-none'
    case '碎碎念': return 'bg-yellow-500 text-white px-4 py-2 rounded-full focus:outline-none'
    case 'Help': return 'bg-purple-500 text-white px-4 py-2 rounded-full focus:outline-none'
    default: return 'bg-gray-500 text-white px-4 py-2 rounded-full focus:outline-none'
  }
}

const getAvatar = (author) => {
  if (!author) {
    return 'https://via.placeholder.com/50'  // 默认头像 URL
  }
  return `https://ui-avatars.com/api/?name=${author}&background=random`  // 使用 ui-avatars 生成头像
}

const onLanguageChanged = (language) => {
  selectedLanguage.value = language;
  fetchArticles(null);
  fetchCategories();
}

onMounted(() => {
  fetchArticles(null)
  fetchCategories()
  // 监听全局语言变化事件
  window.addEventListener('language-change', (event) => {
    onLanguageChanged(event.detail);
  });
})

onBeforeUnmount(() => {
  // 取消全局语言变化事件监听
  window.removeEventListener('language-change', (event) => {
    onLanguageChanged(event.detail);
  });
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
