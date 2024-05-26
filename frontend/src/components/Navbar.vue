<template>
  <nav class="bg-gray-800 text-white p-4 flex justify-between items-center">
    <div class="container mx-auto flex justify-between items-center">
      <span class="text-xl text-white font-semibold">Lafdrue</span>
      <div class="flex items-center space-x-4">
        <router-link to="/" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium" aria-current="page">首页</router-link>
        <router-link to="/products" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">商店</router-link>
        <router-link to="/articles" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">文章</router-link>
        <router-link to="/login" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">登录</router-link>
        <Cart />
        <n-dropdown trigger="hover" @select="changeLanguage" :options="languageOptions">
          <button class="flex items-center text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">
            {{ selectedLanguage }}
            <n-icon size="18" class="ml-1">
              <template #default>
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 011.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </template>
            </n-icon>
          </button>
        </n-dropdown>
      </div>
    </div>
  </nav>
</template>

<script>
import Cart from './Cart.vue';
import { ref } from 'vue';
import { NDropdown, NIcon } from 'naive-ui';

export default {
  components: {
    Cart,
    NDropdown,
    NIcon
  },
  name: 'Navbar',
  setup() {
    const selectedLanguage = ref('English'); // 默认语言为英语

    const languageOptions = [
      { label: 'English', key: 'en' },
      { label: '中文', key: 'zh' }
    ];

    const changeLanguage = (key) => {
      selectedLanguage.value = key === 'en' ? 'English' : '中文';
      const event = new CustomEvent('language-change', { detail: key });
      window.dispatchEvent(event);
    };

    return {
      selectedLanguage,
      languageOptions,
      changeLanguage
    };
  }
};
</script>

<style scoped>
/* 样式不变 */
</style>
