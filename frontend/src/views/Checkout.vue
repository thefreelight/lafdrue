<template>
  <div class="container mx-auto p-8">
    <h2 class="text-2xl font-bold text-center mb-6">结算</h2>
    <div class="flex justify-center">
      <div class="w-full max-w-lg">
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">

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
                id="email" type="email" placeholder="您的邮箱">
          </div>


          <!-- 支付方式选择 -->
          <div class="mb-4">
            <span class="block text-gray-700 text-sm font-bold mb-2">支付方式</span>
            <div class="flex flex-col">
              <label class="inline-flex items-center mt-3">
                <input type="radio" class="form-radio h-5 w-5 text-blue-600" name="paymentMethod" value="alipay"
                       checked>
                <span class="ml-2 text-gray-700">支付宝</span>
              </label>
              <label class="inline-flex items-center mt-3">
                <input type="radio" class="form-radio h-5 w-5 text-green-500" name="paymentMethod" value="wechat">
                <span class="ml-2 text-gray-700">微信支付</span>
              </label>
              <label class="inline-flex items-center mt-3">
                <input type="radio" class="form-radio h-5 w-5 text-red-500" name="paymentMethod" value="stripe">
                <span class="ml-2 text-gray-700">Stripe</span>
              </label>
              <label class="inline-flex items-center mt-3">
                <input type="radio" class="form-radio h-5 w-5 text-yellow-500" name="paymentMethod" value="paypal">
                <span class="ml-2 text-gray-700">PayPal</span>
              </label>
            </div>
          </div>

          <!-- 提交按钮 -->
          <div class="flex justify-end mt-4">
            <button @click="submitOrder" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              提交订单
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import axios from '../axios'; // 确保你已经安装并正确配置了axios

export default {
  name: 'Checkout',
  computed: {
    ...mapState('cart', ['items']),
    totalPrice() {
      return this.items.reduce((total, item) => total + item.quantity * item.price, 0);
    },
    selectedPaymentMethod() {
      // 这里应该是绑定到radio buttons的数据属性
      // 确保这个数据属性能够反映当前用户选择的支付方式
      return this.$store.state.selectedPaymentMethod;
    }
  },
  methods: {
    submitOrder() {
      const orderData = {
        items: this.items,
        totalAmount: this.totalPrice,
        paymentMethod: this.selectedPaymentMethod,
        // 其他订单相关信息，比如用户信息等
      };

      // 发送订单数据到后端
      axios.post('/orders/', orderData)
        .then(response => {
          // 假设后端返回了支付页面所需的信息
          const paymentInfo = response.data;
          // 导航到支付页面，并传递支付信息
          this.$router.push({ name: 'Payment', params: { paymentInfo } });
        })
        .catch(error => {
          console.error('订单提交失败:', error);
          // 这里应该处理错误，比如显示一个错误消息给用户
        });
    }
  }
};
</script>


