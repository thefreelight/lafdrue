<template>
  <div>
    <h1>购物车</h1>
    <div v-for="item in cartItems" :key="item.id" class="cart-item">
      <h3>{{ item.name }}</h3>
      <p>数量: {{ item.quantity }}</p>
      <button @click="updateQuantity(item, item.quantity - 1)" :disabled="item.quantity <= 1">-</button>
      <button @click="updateQuantity(item, item.quantity + 1)">+</button>
      <button @click="removeFromCart(item)">移除</button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex';

export default {
  computed: {
    ...mapState('cart', ['cartItems']),
    ...mapGetters('cart', ['cartTotal', 'cartItemCount']),
  },
  methods: {
    ...mapActions('cart', [
      'addToCart',
      'removeFromCart',
      'incrementItemQuantity',
      'decrementItemQuantity',
    ]),
    // 你可以在这里添加按钮点击事件的方法，调用上面映射的 Vuex actions
  },
};
</script>
