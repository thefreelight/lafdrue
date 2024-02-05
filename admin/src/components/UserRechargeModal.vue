<template>
  <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" v-show="showRechargeModal">
    <div class="relative bg-white rounded-lg p-8 m-auto flex flex-col max-w-md">
      <h3 class="text-xl font-semibold mb-4">充值操作</h3>
      <label class="block mb-2 text-sm font-bold text-gray-700" for="balance">余额充值:</label>
      <input type="number" v-model="balance" class="mb-4 w-full px-3 py-2 border rounded">

      <label class="block mb-2 text-sm font-bold text-gray-700" for="commission">佣金充值:</label>
      <input type="number" v-model="commission" class="mb-6 w-full px-3 py-2 border rounded">

      <div class="flex justify-end">
        <button @click="closeModal" class="px-4 py-2 mr-2 text-gray-700 transition-colors duration-150 border border-gray-300 rounded-lg focus:outline-none">取消</button>
        <button @click="submitRecharge" class="px-4 py-2 text-white transition-colors duration-150 bg-blue-600 border border-transparent rounded-lg hover:bg-blue-700 focus:outline-none">确认充值</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from "../axios";

// 定义 'showRechargeModal' 作为 prop 来控制可见性
const props = defineProps({
  selectedUserId: Number,
  showRechargeModal: Boolean
});

const emit = defineEmits(['update:showRechargeModal']);

const balance = ref(0);
const commission = ref(0);

const closeModal = () => {
  emit('update:showRechargeModal', false);
};

const submitRecharge = async () => {
  try {
    const response = await axios.post('/api/v1/recharge/', {
      user_id: props.selectedUserId,
      balance: balance.value,
      commission: commission.value
    });
    closeModal();
    emit('recharge-success', response.data);
  } catch (error) {
    console.error('Recharge failed:', error);
  }
};
</script>


<style scoped>
/* Your CSS styles */
</style>
