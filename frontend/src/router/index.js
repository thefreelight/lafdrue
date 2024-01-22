import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Products from '../components/ProductList.vue'; // 确保已经创建了这个视图组件
import Cart from '../components/Cart.vue';
import Checkout from '../views/Checkout.vue';
import ProductDetails from "../components/ProductDetails.vue";
import PaymentPage from '../views/PaymentPage.vue';


const routes = [
  { path: '/', component: Home },
  { path: '/login', name: 'Login', component: Login},
  { path: '/register', component: Register },
  { path: '/products', component: Products },
  { path: '/cart', component: Cart },
  { path: '/checkout', component: Checkout },
  { path: '/payment', component: PaymentPage },
  { path: '/products/:id', name: 'ProductDetails', component: ProductDetails }
  // 其他路由...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
