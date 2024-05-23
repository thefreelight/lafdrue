<template>
  <div class="p-4">
    <div v-for="item in cartItems" :key="item.id" class="flex justify-between items-center">
      <span>{{ item.name }}</span>
      <span>{{ item.quantity }}</span>
    </div>
    <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 mt-4" @click="checkout">
      结账
    </button>
  </div>
</template>

<script>
export default {
  name: 'ShoppingCart',
  data() {
    return {
      cartItems: [
        // 示例购物车数据
        { id: 1, name: '产品 1', quantity: 2 },
        // 更多项...
      ]
    };
  },
  methods: {
    checkout() {
      // 实现结账逻辑
      alert('结账功能尚未实现。');
    }
  }
}
</script>
