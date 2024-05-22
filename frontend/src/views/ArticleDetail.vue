<template>
  <div class="container mx-auto p-4">
    <n-card v-if="article" class="mb-6 p-4 border rounded">
      <h1 class="text-3xl font-bold mb-4">{{ article.title }}</h1>
      <n-divider />
      <p class="text-gray-600 mb-4">分类: {{ article.category.name }}</p>
      <div v-html="article.content" class="prose"></div>
    </n-card>
    <div v-else class="text-gray-500">文章不存在</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import { useMessage } from 'naive-ui'
import { useRoute } from 'vue-router'

const article = ref(null)
const message = useMessage()
const route = useRoute()

const fetchArticle = async (id) => {
  try {
    const response = await axios.get(`/api/v1/articles/${id}`)
    article.value = response.data
  } catch (error) {
    message.error('获取文章详情失败')
  }
}

onMounted(() => {
  fetchArticle(route.params.id)
})
</script>
