<template>
  <div class="container mx-auto p-4">
    <n-card class="mb-6 p-4 border rounded">
      <h1 class="text-3xl font-bold mb-4 text-center">博客文章</h1>
      <n-divider />
      <div v-if="articles.length === 0" class="text-gray-500">暂无文章</div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <n-card
            v-for="article in articles"
            :key="article.id"
            class="border rounded-lg hover:shadow-lg transition-shadow duration-300"
        >
          <h2 class="text-2xl font-semibold mb-2">{{ article.title }}</h2>
          <p class="text-gray-600 mb-4">{{ article.content.substring(0, 100) }}...</p>
          <router-link :to="`/articles/${article.id}`" class="text-blue-500 hover:underline">
            阅读更多
          </router-link>
        </n-card>
      </div>
    </n-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import { useMessage } from 'naive-ui'

const articles = ref([])
const message = useMessage()

const fetchArticles = async () => {
  try {
    const response = await axios.get('/api/v1/articles/')
    articles.value = response.data.items
  } catch (error) {
    message.error('获取文章列表失败')
  }
}

onMounted(() => {
  fetchArticles()
})
</script>
