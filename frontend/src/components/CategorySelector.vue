<template>
  <div class="product-list">
    <div class="product" v-for="product in filteredProducts" :key="product.id">
      <h2>{{ product.name }}</h2>
      <p>{{ product.description }}</p>
      <!-- 更多产品信息 -->
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'ProductList',
  computed: {
    ...mapState(['products']),
    filteredProducts() {
      if (!this.categoryId) {
        return this.products;
      }
      return this.products.filter(p => p.categoryId === this.categoryId);
    }
  },
  props: {
    categoryId: String
  }
};
</script>

<style>
/* 添加所需的样式 */
</style>
