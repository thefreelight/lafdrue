<template>
  <n-message-provider>
    <Navbar />
    <router-view />
  </n-message-provider>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar
  },
  mounted() {
    // 监听语言切换事件
    window.addEventListener('language-change', this.onLanguageChange);
  },
  beforeUnmount() {
    // 移除事件监听器
    window.removeEventListener('language-change', this.onLanguageChange);
  },
  methods: {
    onLanguageChange(event) {
      const language = event.detail;
      // 在这里可以根据需要重新获取数据或更新应用状态
      this.$root.$emit('language-changed', language);
    }
  }
}
</script>
