// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from '../components/LoginComponent.vue';
import CardListComponent from '../components/CardListComponent.vue';

const routes = [
  { path: '/login', component: LoginComponent },
  { path: '/cards', component: CardListComponent }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
