<template>
  <div v-if="product" class="product-detail">
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <p>价格: {{ product.price }}</p>
    <button @click="addToCart">加入购物车</button>
  </div>
  <div v-else>
    <p>商品加载中或不存在...</p>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  computed: {
    ...mapState('products', ['products']),
    product() {
      return this.products.find(p => p.id === this.id);
    },
  },
  methods: {
    ...mapActions('cart', ['addToCartAction']),
    addToCart() {
      if (this.product) {
        this.addToCartAction(this.product);
      }
    },
  },
};
</script>
