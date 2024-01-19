<!-- 在 ProductItem.vue -->
<template>
  <div class="product-item">
    <!-- 产品信息 -->
    <button @click="addToCart(product)">添加到购物车</button>
  </div>
</template>

<script>
export default {
  props: {
    product: Object
  },
  methods: {
    addToCart(product) {
      this.$store.dispatch('addToCart', product);
    }
  }
}
</script>
