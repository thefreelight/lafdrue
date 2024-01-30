<template>
  <div class="container mx-auto p-8">
    <div class="flex flex-col items-center">
      <!-- Green check icon -->
      <div class="text-green-500 rounded-full bg-green-100 p-5 inline-flex items-center justify-center mb-6">
        <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <h2 class="text-3xl font-bold text-center text-green-600 mb-6">支付成功</h2>
    </div>
    <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="text-center mb-8">
        <h3 class="text-xl font-bold mb-4">订单详情</h3>
        <div class="text-left inline-block">
          <p class="mb-2"><strong>订单号：</strong>{{ orderDetails.out_trade_no }}</p>
          <p class="mb-2"><strong>支付金额：</strong>{{ orderDetails.money }}</p>
          <p class="mb-2"><strong>支付方式：</strong>{{ orderDetails.type }}</p>
          <p class="mb-2"><strong>商品名称：</strong>{{ orderDetails.name }}</p>
        </div>
      </div>

      <div class="text-center">
        <h3 class="text-xl font-bold mb-4 mt-6">卡密信息</h3>
        <div class="text-left inline-block">
          <!-- Assume you have an array of card information in your data -->
          <ul>
            <li v-for="card in cards" :key="card.id">
              {{ card.info }}
            </li>
          </ul>
        </div>
      </div>

      <div class="text-center mt-6">
        <router-link to="/" class="bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline transition-colors duration-300 ease-in-out">
          返回首页
        </router-link>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';

export default {
  setup() {
    const route = useRoute();
    const store = useStore();
    const orderDetails = ref({});



    onMounted(() => {
      // 解析URL中的查询参数
      orderDetails.value = {
        out_trade_no: route.query.out_trade_no,
        money: route.query.money,
        type: route.query.type,
        name: route.query.name,
        // 其他所需数据...
      };

        // 清空购物车
      store.dispatch('cart/clearCart');
      // 这里可以添加获取卡密信息的逻辑
    });

    return {
      orderDetails,
    };
  },
};
</script>


