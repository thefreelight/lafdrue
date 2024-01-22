<template>
  <div class="relative inline-block text-right">
    <!-- Cart Icon with Badge -->
<div @click="toggleDropdown" class="cursor-pointer">
      <!-- FontAwesome Icon -->
      <font-awesome-icon :icon="['fas', 'shopping-cart']" class="text-white text-xl" />
      <!-- Conditional Badge -->
      <span v-if="totalItems" class="badge">
        {{ totalItems }}
      </span>
    </div>
    <!-- Dropdown Menu -->
    <div v-if="isDropdownVisible" class="absolute right-0 z-50 w-64 mt-2 bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Dropdown content -->
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      isDropdownVisible: false,
      cartCount: 0, // 购物车商品计数
    };
  },
  computed: {
    // 使用 Vuex getter 来获取购物车物品总数
    ...mapGetters('cart', ['totalItems','isDropdownVisible'])
  },
  methods: {
    ...mapActions('cart', ['toggleCartDropdown']),
    toggleDropdown() {
      this.toggleCartDropdown();
    },
    addToCart() {
      // 增加购物车商品数量
      this.cartCount++;
    },
  },
};
</script>

<style scoped>
.badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background-color: red;
  color: white;
  border-radius: full;
  padding: 0.5rem;
  font-size: 0.75rem;
  text-align: center;
}
</style>