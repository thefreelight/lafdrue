import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import './style.css';  // 确保路径与您的文件结构相匹配



const app = createApp(App);
app.use(router);
app.mount('#app');
