<template>
  <nav class="bg-gray-800 text-white p-4 flex justify-between items-center">
    <div class="container mx-auto flex justify-between items-center">
      <span class="text-xl text-white font-semibold">Logo</span>
    <div class="flex items-center space-x-4">
        <router-link to="/" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium" aria-current="page">首页</router-link>
        <router-link to="/products" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">商店</router-link>
        <!-- Assume CartIcon is a component that already has styling -->
        <router-link to="/login" class="text-white hover:text-gray-300 px-3 py-2 rounded-md text-sm font-medium">登录</router-link>
        <cart />
      </div>
    </div>
  </nav>
</template>

<script>
import Cart from './Cart.vue';

export default {
  components: {
    Cart,
  },
  name: 'Navbar',
}
</script>

