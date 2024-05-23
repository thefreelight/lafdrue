<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-200">
    <div class="p-10 bg-white rounded-lg shadow-xl max-w-lg w-full">
      <h1 class="text-3xl font-semibold text-center text-gray-800 mb-6">用户登录</h1>
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">邮箱:</label>
          <input type="email" id="email" v-model="email" placeholder="请输入邮箱" required
                 class="mt-1 p-2 w-full border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500">
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">密码:</label>
          <input type="password" id="password" v-model="password" placeholder="请输入密码" required
                 class="mt-1 p-2 w-full border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500">
        </div>
        <!-- 错误信息展示区域 -->
        <div v-if="errorMessage" class="mb-4 text-center text-red-500">
          {{ errorMessage }}
        </div>
        <div class="flex items-center justify-between">
          <button type="submit"
                  class="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            登录
          </button>
          <router-link to="/register" class="text-sm text-indigo-600 hover:text-indigo-800">没有账号？立即注册
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from '../axios'; // 确保你已经安装并配置了axios
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const errorMessage = ref('');
    const router = useRouter();

    // 检查用户是否已登录
    const checkLoginStatus = () => {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        // 假设我们有一种方式来验证Token的有效性，这里简化处理直接跳转
        router.push('/admin/home');
      }
    };

    const submitForm = async () => {
      // 使用URLSearchParams构造表单数据
      const formData = new URLSearchParams();
      formData.append('username', email.value);
      formData.append('password', password.value);

      try {
        const response = await axios.post('/api/v1/token/', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        });

        // 登录成功，保存Token
        localStorage.setItem('access_token', response.data.access_token);
        // 清除错误信息
        errorMessage.value = '';
        // 页面跳转到管理员首页
        router.push('/admin/home');
      } catch (error) {
        // 显示错误信息
        errorMessage.value = error.response && error.response.data && error.response.data.detail
            ? error.response.data.detail
            : '登录失败，请稍后再试。';
      }
    };

    onMounted(() => {
      checkLoginStatus();
    });

    return {
      email,
      password,
      errorMessage,
      submitForm,
    };
  },
};
</script>

