<template>
  <div class="container mx-auto p-4">
    <!-- Header Section -->
    <div class="bg-gradient-to-r from-green-400 to-blue-500 rounded-lg p-10 text-center text-4xl text-white font-semibold mb-10 font-custom">
      Do more useless things
    </div>

    <!-- Tags Section -->
    <div class="flex justify-center space-x-4 mb-10">
      <n-tag type="success">All</n-tag>
      <n-tag type="info">Genesis</n-tag>
      <n-tag type="warning">碎碎念</n-tag>
      <n-tag type="primary">Help</n-tag>
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
          <img src="https://via.placeholder.com/50" alt="Author" class="w-10 h-10 rounded-full mr-4">
          <div>
            <span class="text-gray-400">{{ article.author || 'Unknown' }}</span>
            <n-tag type="success" class="ml-2">Genesis</n-tag>
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
const message = useMessage()

const fetchArticles = async () => {
  try {
    const response = await axios.get('/api/v1/articles/', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    articles.value = response.data.items  // 从分页对象中提取文章列表
  } catch (error) {
    message.error('获取文章列表失败')
  }
}

onMounted(() => {
  fetchArticles()
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
