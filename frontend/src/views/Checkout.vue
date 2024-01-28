<template>
  <div class="container mx-auto p-8">
    <h2 class="text-2xl font-bold text-center mb-6">结算</h2>
    <div class="flex justify-center">
      <div class="w-full max-w-lg">
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" @submit.prevent="submitOrder">

          <!-- 商品价格明细 -->
          <div class="mb-4">
            <h3 class="text-xl font-bold mb-2">商品明细</h3>
            <ul>
              <li v-for="item in items" :key="item.id" class="flex justify-between py-2 border-b">
                <span>{{ item.name }}</span>
                <span>{{ item.quantity }} x {{ item.price }}</span>
              </li>
            </ul>
          </div>

          <!-- 总价 -->
          <div class="text-right font-bold mb-4">
            <span>总价：</span>
            <span>{{ totalPrice }}</span>
          </div>

          <!-- 邮箱输入 -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
              邮箱
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email" type="email" placeholder="您的邮箱" v-model="userEmail">
          </div>


          <!-- 支付方式列表 -->
          <div class="text-lg font-medium mb-4">请选择支付方式：</div>
          <div class="grid grid-cols-1 gap-4">
            <div v-for="method in paymentMethods"
                 :key="method.id"
                 class="p-4 border rounded-lg cursor-pointer hover:shadow-md"
                 :class="{ 'ring-2 ring-indigo-600': method.id === selectedPaymentMethod?.id }"
                 @click="selectPaymentMethod(method)">
              <div class="flex items-center">
                <!-- <img :src="method.logoUrl" alt="" class="h-8 w-8 object-contain mr-3"> 可选的logo -->
                <div>{{ method.name }}</div>
              </div>
            </div>
          </div>

          <!-- 提交按钮 -->
          <div class="mt-6">
            <button v-if="!paymentUrlGenerated" type="submit"
                    class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline transition-colors duration-300 ease-in-out">
              提交订单
            </button>
            <button v-else @click="goToPaymentPage"
                    class="w-full bg-green-600 text-white font-bold py-2 px-4 rounded hover:bg-green-700 focus:outline-none focus:shadow-outline transition-colors duration-300 ease-in-out">
              继续支付
            </button>
          </div>
        </form>
      </div>
    </div>
    <!-- 模态框组件用于显示警告或错误 -->
    <Modal v-if="showModal" @close="showModal = false">
      <p>{{ modalMessage }}</p>
    </Modal>
  </div>


</template>

<script>
import axios from '../axios';
import {mapState, mapActions} from 'vuex';
import Modal from '../components/Modal.vue';

export default {
  components: {Modal},
  data() {
    return {
      userEmail: '',
      cartItems: [],
      isSubmitting: false,
      showModal: false,
      modalMessage: '',
      selectedPaymentMethod: null,
      paymentMethods: [],
      paymentUrlGenerated: false,
      paymentUrl: null,
    };
  },
  computed: {
    ...mapState('cart', ['items']),
    totalPrice() {
      return this.items.reduce((total, item) => total + item.quantity * item.price, 0).toFixed(2);
    },
  },
  methods: {
    ...mapActions('cart', ['clearCart', 'loadCart']),
    fetchPaymentMethods() {
      axios.get('/api/v1/payment_methods/').then(response => {
        this.paymentMethods = response.data;
      }).catch(error => {
        this.errorHandler(error);
      });
    },
    submitOrder() {
      if (this.isSubmitting) {
        console.log("提交正在进行中，防止重复提交");
        return;
      }
      this.isSubmitting = true;
      console.log("开始提交订单");

      let orderData = {
        user_email: this.userEmail,
        role: "用户角色", // 需要根据实际情况设定
        payment_method: this.selectedPaymentMethod?.type,  //实际获取的是支付方式里的类别，比如alipay
        client_ip: "用户IP地址", // 需要获取用户IP地址
        total_amount: this.totalPrice, // 计算的总金额
        items: this.items.map(item => ({
          product_id: item.id,
          product_name: item.name, // 假设 item 中已有名称
          shipping_method: "默认配送方式", // 需要根据实际情况设定
          quantity: item.quantity,
          price: item.price
        })),
      };

      axios.post('/api/v1/creat_order/', orderData)
          .then(response => {
            console.log("订单创建成功:", response.data);
            let orderInfo = response.data;
            let paymentUrl = `/api/v1/payment_methods/create_payment_url?payment_method=${encodeURIComponent(this.selectedPaymentMethod?.payment_method)}`;

            return axios.post(paymentUrl, orderInfo);
          })
          .then(response => {
            if (response.data && response.data.payment_url) {
              console.log("支付URL创建成功:", response.data.payment_url);
              this.paymentUrl = response.data.payment_url;
              this.paymentUrlGenerated = true; // 更新标志
            } else {
              throw new Error("支付URL未正确返回");
            }
          })
          .catch(error => {
            console.error("提交订单或创建支付URL时发生错误:", error);
            this.errorHandler(error);
          })
          .finally(() => {
            this.isSubmitting = false;
          });
    },
    goToPaymentPage() {
      window.location.href = this.paymentUrl;
    },
    errorHandler(error) {
      this.modalMessage = error.response?.data?.detail || '发生错误，请稍后再试。';
      this.showModal = true;
    },
    //选择支付方式
    selectPaymentMethod(method) {
      if (this.selectedPaymentMethod?.id === method.id) {
        this.selectedPaymentMethod = null; // Deselect if the same method is clicked again
      } else {
        this.selectedPaymentMethod = method; // Set the selected method
      }
    },
  },
  mounted() {
    this.fetchPaymentMethods(); // 加载支付方式
    if (!this.items.length) {
      this.$store.dispatch('cart/loadCart'); // 从 Vuex 加载购物车内容
    }
  },


};
</script>

