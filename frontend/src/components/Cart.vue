<template>
   <div class="relative">
    <!-- Cart Icon with Conditional Badge -->
    <div @click.stop="toggleDropdown" class="flex items-center cursor-pointer">
      <!-- FontAwesome Icon -->
      <font-awesome-icon icon="shopping-cart" class="text-gray-200 hover:text-gray-100 text-xl"/>
      <!-- Conditional Badge -->
      <span v-if="totalItems > 0" class="absolute -top-2 -right-3 inline-block text-xs px-2 py-1 leading-none text-white bg-blue-600 rounded-full">
        {{ totalItems }}
      </span>
    </div>

    <!-- Dropdown Menu -->
    <div v-if="isDropdownVisible" class="absolute right-0 mt-2 w-64 bg-white rounded-md shadow-lg z-20">
      <p class="text-gray-700 px-4 py-2 border-b border-gray-100">我的购物车</p>
      <ul class="text-gray-700">
        <li v-for="item in items" :key="item.id" class="px-4 py-2 hover:bg-gray-100 flex justify-between items-center">
          {{ item.name }} - {{ item.quantity }} x {{ item.price }}
          <button @click="removeFromCart(item.id)" class="ml-4 text-red-600 hover:text-red-800">
            &times;
          </button>
        </li>
      </ul>
      <div class="px-4 py-3 flex justify-end">
      <router-link to="/checkout" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          结算
      </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState, mapMutations, mapActions,mapGetters} from 'vuex';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
  components: {
    FontAwesomeIcon
  },
  mounted() {
    this.$store.dispatch('cart/loadCart');
    // 添加全局点击事件监听器，用于关闭购物车下拉菜单
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
  document.removeEventListener('click', this.handleClickOutside);
},
  computed: {
    ...mapGetters('cart', ['totalItems','isDropdownVisible']),
    ...mapState('cart', ['items'])

  },
  methods: {
  ...mapActions('cart', ['addToCart', 'removeFromCart', 'toggleCartDropdown', 'loadCart']),
     toggleDropdown() {
    // 只有当下拉菜单不可见时，才打开它
    if (!this.isDropdownVisible) {
      this.toggleCartDropdown();
    }
  },
     handleClickOutside(event) {
    // 只有当下拉菜单是可见的，并且点击的不是购物车组件内部时，才关闭它
    if (this.isDropdownVisible && !this.$el.contains(event.target)) {
      this.toggleCartDropdown();
    }
  },

  },
};
</script>


