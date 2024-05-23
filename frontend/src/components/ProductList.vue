<template>
  <div class="container mx-auto mt-10">
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white">
        <thead class="text-white bg-gray-800">
          <tr>
            <th class="py-3 px-4 uppercase font-semibold text-sm">商品名称</th>
            <th class="py-3 px-4 uppercase font-semibold text-sm">库存</th>
            <th class="py-3 px-4 uppercase font-semibold text-sm">价格</th>
            <th class="py-3 px-4 uppercase font-semibold text-sm">操作</th>
          </tr>
        </thead>
        <tbody class="text-gray-700">
          <tr v-for="product in products" :key="product.id" class="border-t hover:bg-gray-100">
            <td class="py-3 px-4">{{ product.name }}</td>
            <td class="py-3 px-4">{{ product.stock }} pcs</td>
            <td class="py-3 px-4">${{ product.price }}</td>
            <td class="py-3 px-4 flex justify-end items-center">
              <button @click="handleAddToCart(product)"
                      class="bg-green-500 text-white active:bg-green-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button">
                加入购物车
              </button>
              <button @click="buyProduct(product)"
                      class="bg-blue-500 text-white active:bg-blue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button">
                购买
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Modal组件的使用 -->
  <Modal :isVisible="showModal" :message="modalMessage" @close="showModal = false"/>
</template>


<script>
import axios from '../axios';
import { mapGetters, mapActions } from 'vuex';
import Modal from "./Modal.vue";


export default {
  components: {
    Modal
  },
  data() {
    return {
      showModal: false,
      modalMessage: '',
      products: [],
    };
  },
  async created() {
    try {
      const response = await axios.get('/api/v1/products/');
      this.products = response.data;
    } catch (error) {
      console.error('There was an error fetching the products:', error);
    }
  },
  computed: {
    ...mapGetters('cart', ['totalItems']),
  },
  methods: {
    ...mapActions('cart', ['addToCart','saveCart']),

    // 重命名组件内的方法以避免与 Vuex action 冲突
    handleAddToCart(product) {
    // 首先检查库存
    if (product.stock <= 0) {
      this.modalMessage = '抱歉，该商品库存不足，无法购买。';
      this.showModal = true;
    } else {
      // 如果库存足够，添加到购物车
      this.addToCart(product).then(() => {
        // 商品添加到购物车后，保存购物车状态
        this.saveCart();
      });
    }
  },
    buyProduct(product) {
      // TODO: 实现购买商品的逻辑
      // 使用编程式导航跳转到商品详情页
      if (product.stock === 0) {
        this.modalMessage = '抱歉，该商品库存不足，无法购买。';
        this.showModal = true;
        return;
      }
      const router = this.$router;
      router.push({ name: 'ProductDetails', params: { id: product.id } });
    },
    closeModal() {
      this.showModal = false;
    },
  },
};
</script>


