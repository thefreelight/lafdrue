import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import './style.css';  // 确保路径与您的文件结构相匹配
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUserSecret } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


library.add(faUserSecret) // 添加图标到库


const app = createApp(App);
// 全局注册图标组件
app.component('font-awesome-icon', FontAwesomeIcon);

app.use(router);
app.mount('#app');


