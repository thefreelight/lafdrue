<template>
  <div class="min-h-screen flex items-center justify-center" :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="bg-white bg-opacity-75 rounded-lg p-10 shadow-xl">
      <div class="mb-4">
        <h1 class="text-xl text-center font-semibold">{{ quote.cn }} | {{ quote.en }}</h1>
      </div>
      <form @submit.prevent="submitForm" class="space-y-6">
        <div class="space-y-1">
          <label for="email" class="text-sm font-medium">邮箱:</label>
          <input id="email" type="email" placeholder="请输入您的邮箱" v-model="email" required
                 class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:border-indigo-500">
        </div>
        <div class="space-y-1">
          <label for="password" class="text-sm font-medium">密码:</label>
          <input id="password" type="password" placeholder="请输入您的密码" v-model="password" required
                 class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:border-indigo-500">
        </div>
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <input type="text" v-model="captchaInput" placeholder="验证码"
                   class="w-2/3 px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:border-indigo-500">
            <img :src="captchaImage" @click="refreshCaptcha" class="w-1/3 h-12 cursor-pointer">
          </div>
        </div>
        <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:border-indigo-700 focus:ring-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
          登录
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const captchaInput = ref('');
    const captchaImage = ref('');
    const quote = ref({ cn: '', en: '' });
    const backgroundImage = ref('');

    const fetchQuote = async () => {
      try {
        const response = await axios.get('https://v1.hitokoto.cn?c=i&encode=json');
        quote.value = response.data;
      } catch (error) {
        console.error('Error fetching quote:', error);
      }
    };

    const fetchBackgroundImage = async () => {
      try {
        const response = await axios.get('https://source.unsplash.com/random/1920x1080?sci-fi');
        backgroundImage.value = response.request.responseURL;
      } catch (error) {
        console.error('Error fetching background image:', error);
      }
    };

    const refreshCaptcha = async () => {
      // Replace with your captcha API
      captchaImage.value = 'path-to-captcha-api';
    };

    const submitForm = () => {
      // Implement your login logic here
      console.log('Submitting:', email.value, password.value, captchaInput.value);
    };

    onMounted(async () => {
      await fetchQuote();
      await fetchBackgroundImage();
      await refreshCaptcha();
    });

    return {
      email,
      password,
      captchaInput,
      captchaImage,
      quote,
      backgroundImage,
      refreshCaptcha,
      submitForm,
    };
  },
};
</script>


