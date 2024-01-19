import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Products from '../components/ProductList.vue'; // 确保已经创建了这个视图组件
import Cart from '../views/Cart.vue';
import Checkout from '../views/Checkout.vue';
import ProductDetail from '../views/ProductDetail.vue'; // 引入商品详情组件


const routes = [
  { path: '/', component: Home },
  { path: '/login', name: 'Login', component: Login},
  { path: '/register', component: Register },
  { path: '/products', component: Products },
  { path: '/cart', component: Cart },
  { path: '/checkout', component: Checkout },
  { path: '/product/:id', name: 'ProductDetail', component: ProductDetail },

  // 其他路由...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
