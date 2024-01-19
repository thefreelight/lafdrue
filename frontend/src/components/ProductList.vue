// src/components/ProductList.vue
<template>
  <div class="product-list-container">
    <table class="table">
      <thead>
        <tr>
          <th>商品名称</th>
          <th>库存</th>
          <th>价格</th>
          <th class="actions-header"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id" class="product-row">
          <td>{{ product.name }}</td>
          <td>{{ product.stock }} pcs</td>
          <td>${{ product.price }}</td>
          <td class="actions">
            <button @click="handleAddToCart(product)" class="btn btn-cart">加入购物车</button>
            <button @click="buyProduct(product)" class="btn btn-buy">购买</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import axios from '../axios';
import { mapGetters, mapActions } from 'vuex';


export default {
  data() {
    return {
      products: [],
    };
  },
  async created() {
    try {
      const response = await axios.get('/products/');
      this.products = response.data;
    } catch (error) {
      console.error('There was an error fetching the products:', error);
    }
  },
  computed: {
    ...mapGetters('cart', ['totalItems']),
  },
  methods: {
    ...mapActions('cart', ['addToCart', 'toggleCartDropdown']),

    // ...fetchProducts, fetchCategories, etc.
    // 重命名组件内的方法以避免与 Vuex action 冲突
    handleAddToCart(product) {
      // 调用 Vuex action
      this.addToCart(product);
    },
    buyProduct(product) {
      // TODO: 实现购买商品的逻辑
      alert(`产品 "${product.name}" 购买成功。`);
      console.log('Product purchased:', product);
    }
  }
};
</script>

<style scoped>
.product-list-container {
  max-width: 1000px;
  margin: auto;
  border-collapse: collapse;
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table thead {
  background-color: #4CAF50;
}

.table thead th {
  color: white;
  padding: 15px;
  text-align: left;
}

.actions-header {
  text-align: right;
}

.product-row {
  transition: background-color 0.3s ease;
}

.product-row:hover {
  background-color: #f5f5f5;
}

.actions {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
}

.btn {
  padding: 10px 20px;
  margin-left: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-cart {
  background-color: #5cb85c;
  color: white;
}

.btn-cart:hover {
  background-color: #4cae4c;
}

.btn-buy {
  background-color: #007bff;
  color: white;
}

.btn-buy:hover {
  background-color: #0056b3;
}
</style>

