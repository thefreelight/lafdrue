<template>
  <div class="product-card border rounded overflow-hidden shadow-lg m-4">
    <img :src="product.image" alt="product.name" class="w-full" />
    <div class="p-4">
      <h3 class="product-name font-bold text-xl mb-2">{{ product.name }}</h3>
      <p class="product-description text-gray-700 text-base">{{ product.description }}</p>
      <div class="product-price mt-3 font-semibold text-gray-900">{{ product.price | currency }}</div>
      <button @click="addToCart(product)" class="add-to-cart bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mt-4">
        添加到购物车
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  methods: {
    addToCart(product) {
      // 触发一个事件来添加商品到购物车
      this.$emit('add-to-cart', product);
    },
  },
  filters: {
    currency(value) {
      return `¥${parseFloat(value).toFixed(2)}`;
    },
  },
};
</script>

<style scoped>
.product-card {
  width: 300px;
}
.add-to-cart {
  transition: background-color 0.3s ease;
}
</style>
