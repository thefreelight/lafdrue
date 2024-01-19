<template>
  <div class="cart-icon-container" @click="toggleDropdown">
    <svg class="cart-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="9" cy="21" r="1"></circle>
      <circle cx="20" cy="21" r="1"></circle>
      <path d="M1 1h4l2.6 13.34a1 1 0 0 0 .92.66h10.56a1 1 0 0 0 .92-.66L23 6H6"></path>
    </svg>
    <span class="cart-count">{{ totalItems }}</span>
    <CartDropdown v-if="isDropdownVisible" />
  </div>
</template>

<script>
import { mapGetters, mapActions,mapState } from 'vuex'
import CartDropdown from './CartDropdown.vue';


export default {
  name: 'CartIcon',
  components: {
    CartDropdown
  },
  computed: {
    ...mapGetters('cart', ['totalItems','isDropdownVisible']), // Assuming you have a getter named 'totalItems'

  },
  methods: {
    ...mapActions('cart', ['toggleCartDropdown']),
    toggleDropdown() {
      this.toggleCartDropdown();
    },
  },
};
</script>

<style scoped>
.cart-icon-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.cart-icon {
  width: 24px; /* 调整图标大小 */
  height: auto;
}

.cart-count {
  background-color: #ff3e6c; /* 现代粉红色 */
  color: white;
  border-radius: 12px; /* 保持圆形 */
  padding: 0 6px; /* 上下无填充，左右填充 */
  position: absolute;
  top: -8px; /* 适当调整以确保标记位置正确 */
  right: -8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  line-height: 1.6; /* 控制数字垂直居中 */
  min-width: 16px; /* 保持圆形 */
}
</style>
