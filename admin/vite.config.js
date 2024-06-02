// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  optimizeDeps: {
    include: ['@wangeditor/editor-for-vue']
  },
  server: {
    port: 3000, // 确保端口正确
  }
});
