<template>
  <div class="min-h-screen flex items-center justify-center bg-no-repeat bg-cover"
       :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="w-full max-w-md p-8 space-y-8 bg-white bg-opacity-90 rounded-xl shadow-2xl">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          欢迎登录
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600 mt-5">
          {{ quote.cn }} | {{ quote.en }}
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="submitForm">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email" class="sr-only">邮箱</label>
            <input id="email" name="email" type="email" autocomplete="email" required
                   class="relative block w-full px-3 py-2 rounded-none rounded-t-md border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                   placeholder="请输入您的邮箱" v-model="email">
          </div>
          <div>
            <label for="password" class="sr-only">密码</label>
            <input id="password" name="password" type="password" autocomplete="current-password" required
                   class="relative block w-full px-3 py-2 rounded-none rounded-b-md border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                   placeholder="请输入您的密码" v-model="password">
          </div>
          <!-- 错误信息展示 -->
          <div v-if="errorMessage"
               class="p-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800" role="alert">
            {{ errorMessage }}
          </div>

        </div>

        <div>
          <button type="submit"
                  class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            登录
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from '../axios';
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router'; // 引入vue-router的useRouter函数

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const quote = ref({cn: '', en: ''});
    const backgroundImage = ref('');
    // 使用useRouter来获取router实例
    const router = useRouter();
    const fetchQuote = async () => {
      try {
        // 这里使用的是一言API获取中文名言
        // 如果你需要双语名言，你可能需要寻找或者创建一个支持的API
        const response = await axios.get('https://v1.hitokoto.cn?c=i&encode=json');
        quote.value.cn = response.data.hitokoto;
        quote.value.en = response.data.from_who;
      } catch (error) {
        console.error('获取名言错误:', error);
      }
    };

    const fetchBackgroundImage = async () => {
      try {
        // 这里使用Unsplash的API获取随机科幻背景图
        const response = await axios.get('https://source.unsplash.com/random/1920x1080?sci-fi');
        backgroundImage.value = response.request.responseURL;
      } catch (error) {
        console.error('获取背景图错误:', error);
      }
    };

// 错误信息响应式变量
    const errorMessage = ref('');

    const login = async () => {
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
        // 清除可能存在的旧错误信息
        errorMessage.value = '';

        // 使用Vue Router进行页面跳转
    router.push('/admin/home');
      } catch (error) {
        if (error.response) {
          // 从后端响应中获取错误信息，并显示
          errorMessage.value = error.response.data.detail || '登录失败，请重试';
        } else {
          // 处理其他错误情况
          errorMessage.value = '登录错误，请重试';
        }
        console.error('登录错误:', error);
      }
    };

    const submitForm = () => {
      login()
    };

    onMounted(async () => {
      if (localStorage.getItem('access_token')) {
         router.push('/admin/home');
        }
        await fetchQuote();
        await fetchBackgroundImage();
    });

    return {
      email,
      password,
      quote,
      backgroundImage,
      submitForm,
      errorMessage, // 错误信息响应式变量

    };
  },
};
</script>

