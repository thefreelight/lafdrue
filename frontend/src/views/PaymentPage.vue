<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="w-full max-w-lg p-5 bg-white rounded-lg shadow-xl mx-2">
      <div class="mb-5">
        <h3 class="text-center text-2xl font-medium text-gray-700">确认支付</h3>
        <h5 class="text-center text-lg text-gray-500 mt-2">{{ paymentMethodName }}</h5>
      </div>
      <div class="flex justify-center mb-10">
        <img :src="qrCodeUrl" alt="支付二维码" class="w-64 h-64 object-cover p-2 border border-gray-300 rounded-md" />
      </div>
      <div class="text-center mb-6">
        <p class="text-gray-600">扫描上方二维码以完成支付</p>
        <p class="text-xl text-gray-800 font-bold mt-2">￥{{ totalAmount }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

export default {
  data() {
    return {
      paymentMethod: this.$route.params.paymentMethod,
      qrCodeUrl: '', // 二维码URL
      pollingInterval: null, // 轮询间隔
    };
  },
  computed: {
    ...mapState('cart', ['totalAmount']),
    // ...其他computed属性...
  },
  methods: {
    startPollingPaymentStatus() {
      // 设置轮询间隔，例如每5秒检查一次
      this.pollingInterval = setInterval(() => {
        this.checkPaymentStatus();
      }, 5000);
    },
    checkPaymentStatus() {
      // 假设您有一个API用于检查支付状态
      axios.get(`/api/payment/status?method=${this.paymentMethod}`)
        .then(response => {
          if (response.data.status === 'paid') {
            clearInterval(this.pollingInterval);
            this.$router.push('/payment-success'); // 支付成功后的导航
          }
        })
        .catch(error => {
          console.error('检查支付状态失败:', error);
        });
    }
  },
  mounted() {
    // 获取二维码URL
    axios.get(`/api/payment/qr-code?method=${this.paymentMethod}`)
      .then(response => {
        this.qrCodeUrl = response.data.qrCodeUrl;
      })
      .catch(error => {
        console.error('获取二维码失败:', error);
      });

    // 开始轮询检查支付状态
    this.startPollingPaymentStatus();
  },
  beforeUnmount() {
    // 清除轮询间隔
    if (this.pollingInterval) {
      clearInterval(this.pollingInterval);
    }
  }
};
</script>
