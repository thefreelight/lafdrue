import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index'; // 引入路由配置
import './style.css';  // 确保路径与您的文件结构相匹配
import store from './store/index'; // 引入 store/index.js
import { library } from '@fortawesome/fontawesome-svg-core';
import { faShoppingCart, faChevronDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import naive from 'naive-ui'; // 引入 naive-ui
import i18n from './i18n'; // 引入 i18n 配置


// 添加 FontAwesome 图标
library.add(faShoppingCart, faChevronDown);

const app = createApp(App);

// 使用 Vuex store
app.use(store);

// 使用 Vue Router
app.use(router);

// 使用 naive-ui
app.use(naive);

// 使用 i18n
app.use(i18n);

// 注册 FontAwesomeIcon 组件
app.component('font-awesome-icon', FontAwesomeIcon);

// 在挂载之前加载购物车
store.dispatch('cart/loadCart');

app.mount('#app');
