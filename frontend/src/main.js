import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index'; // 引入路由配置
import './style.css';  // 确保路径与您的文件结构相匹配
import store from './store';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faShoppingCart);



const app = createApp(App);
app.use(store);
app.use(router);
app.mount('#app');

// 注册 FontAwesomeIcon 组件
app.component('font-awesome-icon', FontAwesomeIcon);