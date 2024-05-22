// router/index.js
import {createRouter, createWebHistory} from 'vue-router'
import Login from "../views/Login.vue";
import Home from '../views/Home.vue';
import Dashboard from '../views/Dashboard.vue';
import UserManagement from "../views/UserManagement.vue";
import MembershipLevelManagement from "../views/MembershipLevelManagement.vue";
import CategoryManagement from "../views/CategoryManagement.vue";
import ProductManagement from "../views/ProductManagement.vue";
import CardManagement from "../views/CardManagement.vue";

const routes = [
    {
        path: '/', name: 'Home', component: Home, meta: {requiresAuth: true},
        children: [
            {path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: {requiresAuth: true}},
            {path: '/users', name: 'Users', component: UserManagement, meta: {requiresAuth: true}},
            {path: '/users/levels', name: 'levels', component: MembershipLevelManagement, meta: {requiresAuth: true}},
            { path: '/category/', name: 'CategoryManagement', component: CategoryManagement, meta: { requiresAuth: true } }, // 新增的分类管理路由
            { path: '/product/', name: 'ProductManagement', component: ProductManagement, meta: { requiresAuth: true } },
            { path: '/card/', name: 'CardManagement', component: CardManagement, meta: { requiresAuth: true } },

            // 如果需要让仪表盘成为默认页面，可以添加重定向
            { path: '', redirect: { name: 'Dashboard' } },
        ]
    },
    {path: '/login', name: 'Login', component: Login},


    // ... 其他路由
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('access_token'); // 检查本地存储中是否有token
    if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
        next({name: 'Login'}); // 未登录则跳转到登录页面
    } else {
        next(); // 已登录或不需要验证的页面直接放行
    }
});

export default router
