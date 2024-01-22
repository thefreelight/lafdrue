<template>
  <div class="container mx-auto px-4 h-full flex flex-col justify-center items-center">
    <!-- Loading Spinner -->
    <div v-if="isLoading" class="text-lg text-center">
      正在加载...
    </div>

    <!-- Product Details -->
    <div v-else-if="product" class="flex flex-wrap -mx-4">
      <!-- Product Image -->
      <div class="w-full md:w-1/2 px-4 mb-6 md:mb-0 flex justify-center">
        <img :src="product.image_url || 'default-image.png'" alt="Product Image" class="rounded-lg shadow-lg h-80 object-cover" />
      </div>

      <!-- Product Description and Actions -->
      <div class="w-full md:w-1/2 px-4 flex flex-col justify-center">
        <h1 class="text-2xl font-semibold mb-2">{{ product.name }}</h1>
        <p class="text-lg text-gray-700 mb-4">¥{{ product.price.toFixed(2) }}</p>
        <div class="flex items-center mb-4">
          <button @click="decreaseQuantity" class="text-xl h-10 w-10 rounded-full bg-gray-200 flex justify-center items-center mx-2 focus:outline-none hover:bg-gray-300">-</button>
          <input type="number" v-model="quantity" class="w-16 text-center border border-gray-300 rounded-lg px-2 py-1 mx-2" min="1" />
          <button @click="increaseQuantity" class="text-xl h-10 w-10 rounded-full bg-gray-200 flex justify-center items-center mx-2 focus:outline-none hover:bg-gray-300">+</button>
        </div>
        <button @click="addToCart" class="bg-green-500 text-white rounded-lg px-6 py-2 mb-2 hover:bg-green-600 focus:outline-none">加入购物车</button>
        <button @click="buyNow" class="bg-blue-500 text-white rounded-lg px-6 py-2 hover:bg-blue-600 focus:outline-none">立即购买</button>
      </div>
    </div>

    <!-- Product Extra Details -->
    <div v-if="product" class="w-full px-4 py-8 mt-6 bg-white shadow-lg rounded-lg">
      <h2 class="text-xl font-semibold mb-3">商品详情</h2>
      <p class="text-gray-600">{{ product.description }}</p>
    </div>

    <!-- Error Message -->
    <div v-else class="text-red-500 text-lg">
      无法加载产品详情。
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import axios from '../axios';

export default {
  name: 'ProductDetails',
  data() {
    return {
      product: null,
      quantity: 1,
      selectedPaymentMethod: 'alipay',
      contactInfo: '',
      isLoading: true,
    };
  },
  methods: {
    ...mapActions('cart', ['addToCartAction']),
    fetchProductDetails() {
      const productId = this.$route.params.id;
      this.isLoading = true;
      axios.get(`/products/${productId}`)
        .then(response => {
          if (response.data && typeof response.data.price === 'number') {
            this.product = response.data;
            console.log('Fetched product:', this.product);
          } else {
            console.error('Product data is incomplete:', response.data);
          }
        })
        .catch(error => {
          console.error('Error fetching product details:', error);
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    addToCart() {
      const productToAdd = {
        ...this.product,
        quantity: this.quantity
      };
      this.addToCartAction(productToAdd);
    },
    buyNow() {
      this.$router.push({ name: 'Checkout', params: { product: this.product, quantity: this.quantity } });
    },
    decreaseQuantity() {
      if (this.quantity > 1) {
        this.quantity--;
      }
    },
    increaseQuantity() {
      this.quantity++;
    }
  },
  mounted() {
    this.fetchProductDetails();
  }
};
</script>


