import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Products from '../components/ProductList.vue';
import Cart from '../components/Cart.vue';
import Checkout from '../views/Checkout.vue';
import ProductDetails from "../components/ProductDetails.vue";
import PaymentPage from '../views/PaymentPage.vue';
import PaymentSuccess from '../views/PaymentSuccess.vue';
import ArticleList from '../views/ArticleList.vue';
import ArticleDetail from '../views/ArticleDetail.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', name: 'Login', component: Login},
  { path: '/register', component: Register },
  { path: '/products', component: Products },
  { path: '/cart', component: Cart },
  { path: '/checkout', component: Checkout },
  { path: '/payment', component: PaymentPage },
  { path: '/products/:id', name: 'ProductDetails', component: ProductDetails },
  { path: '/payment-success', name: 'PaymentSuccess', component: PaymentSuccess },
  { path: '/articles', name: 'ArticleList', component: ArticleList },
  { path: '/articles/:id', name: 'ArticleDetail', component: ArticleDetail }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
