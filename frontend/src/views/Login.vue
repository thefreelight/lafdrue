<template>
  <div class="login-container flex items-center justify-center h-screen bg-gray-100">
    <div class="max-w-xs w-full bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h1 class="mb-6 text-center text-2xl font-bold text-gray-700">用户登录</h1>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
            邮箱:
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="请输入邮箱" v-model="email" required>
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            密码:
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="请输入密码" v-model="password" required>
        </div>
        <div class="flex items-center justify-between">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
            登录
          </button>
          <router-link class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" to="/register">
            没有账号？立即注册
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      // 在这里实现登录逻辑
      // ...
    }
  }
};
</script>

<style scoped>
/* 这里添加额外的样式 (如果需要) */
.login-container {
  background-image: url('path-to-your-background-image.jpg'); /* 替换为您的背景图片路径 */
  background-size: cover;
}
</style>
