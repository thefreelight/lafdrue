<template>
  <nav class="p-4 text-white flex justify-between bg-gradient-nav">
    <span class="font-bold">Logo</span>
    <div class="hidden md:flex">
      <router-link to="/" class="px-3 hover:bg-gradient-to-r hover:from-purple-600 hover:to-blue-500">首页</router-link>
      <router-link to="/products" class="px-3 hover:bg-gradient-to-r hover:from-purple-600 hover:to-blue-500">商店</router-link>
      <CartIcon />
      <router-link to="/login" class="px-3 hover:bg-gradient-to-r hover:from-purple-600 hover:to-blue-500">登录</router-link>
    </div>
  </nav>
</template>

<script>
import CartIcon from './CartIcon.vue';

export default {
  components: {
    CartIcon,
  },
  name: 'Navbar',
}
</script>

<style>
/* 根据需要添加样式 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: white;
}
.logo {
  font-weight: bold;
}
</style>