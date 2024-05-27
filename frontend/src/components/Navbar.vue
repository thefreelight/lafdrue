<template>
  <nav class="bg-gray-800 text-white p-4 flex justify-between items-center">
    <div class="container mx-auto flex justify-between items-center">
      <span class="text-xl text-white font-semibold">Lafdrue</span>
      <div class="flex items-center space-x-4">
        <router-link to="/" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium" aria-current="page">{{ translations.home }}</router-link>
        <router-link to="/products" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">{{ translations.products }}</router-link>
        <router-link to="/articles" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">{{ translations.articles }}</router-link>
        <router-link to="/login" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">{{ translations.login }}</router-link>
        <Cart />
        <n-dropdown trigger="hover" @select="changeLanguage" :options="languageOptions">
          <button class="flex items-center text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">
            <span class="flag-icon">{{ selectedLanguage.icon }}</span>
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

<script setup>
import { ref, onMounted } from 'vue';
import axios from '../axios.js';
import { NDropdown, NIcon } from 'naive-ui';
import Cart from './Cart.vue';

const selectedLanguage = ref({ label: 'English', icon: '🇺🇸', key: 'en' }); // 默认语言为英语
const translations = ref({ home: '', products: '', articles: '', login: '' });

const languageOptions = [
  { label: 'English', key: 'en', icon: '🇺🇸' },
  { label: '中文', key: 'zh', icon: '🇨🇳' }
];

const fetchTranslations = async (lang) => {
  try {
    const response = await axios.get(`/api/v1/language/${lang}`);
    translations.value = response.data;
  } catch (error) {
    console.error('Error fetching translations:', error);
  }
};

const changeLanguage = (key) => {
  const selected = languageOptions.find(option => option.key === key);
  if (selected) {
    selectedLanguage.value = selected;
    fetchTranslations(key);
    const event = new CustomEvent('language-change', { detail: key });
    window.dispatchEvent(event);
  }
};

// 初始化时加载默认语言
onMounted(() => {
  console.log('Component mounted, fetching initial translations'); // 
  fetchTranslations(selectedLanguage.value.key);
});
</script>

<style scoped>
.flag-icon {
  font-size: 1.5em; /* 调整字体大小以使 Unicode 图标更明显 */
}
</style>
