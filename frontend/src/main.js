import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index'; // 引入路由配置
import './style.css';  // 确保路径与您的文件结构相匹配
import store from './store';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import naive from 'naive-ui'; // 引入 naive-ui


library.add(faShoppingCart);



const app = createApp(App);
app.use(store);
app.use(router);
app.use(naive); // 使用 naive-ui


app.mount('#app');


// 在挂载之前加载购物车
store.dispatch('cart/loadCart');

// 注册 FontAwesomeIcon 组件
app.component('font-awesome-icon', FontAwesomeIcon);
