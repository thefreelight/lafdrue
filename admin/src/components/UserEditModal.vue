<template>
  <div  class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-8 max-w-xl w-full">
      <h3 class="text-xl font-semibold mb-4">编辑用户</h3>
      <form @submit.prevent="submitForm" class="space-y-6">
        <div class="flex flex-wrap -mx-2">
          <div class="w-full px-2 mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">用户名</label>
            <input v-model="selectedUser.username" type="text" placeholder="用户名" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" required>
          </div>
          <div class="w-full px-2 mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">邮箱</label>
            <input v-model="selectedUser.email" type="email" placeholder="邮箱" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" required>
          </div>
          <div class="w-full px-2 mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="membershipLevel">会员等级</label>
            <select v-model="selectedUser.membership_level_id" class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
              <option v-for="level in membershipLevels" :value="level.id">{{ level.name }}</option>
            </select>
          </div>
          <div class="w-full px-2 mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="referralCode">推荐码</label>
            <input v-model="selectedUser.referral_code" type="text" placeholder="推荐码" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="referralCode">
          </div>
          <div class="w-full px-2 mb-4 flex items-center">
            <label class="block text-gray-700 text-sm font-bold mb-2 mr-4" for="isAgent">是否代理</label>
            <input v-model="selectedUser.is_agent" type="checkbox" class="toggle toggle-accent" id="isAgent">
          </div>
          <div class="w-full px-2 mb-4 flex items-center">
            <label class="block text-gray-700 text-sm font-bold mb-2 mr-4" for="isActive">是否激活</label>
            <input v-model="selectedUser.is_active" type="checkbox" class="toggle toggle-accent" id="isActive">
          </div>
        </div>
        <div class="flex justify-end pt-2">
          <button type="button" @click="closeModal" class="px-4 py-2 mr-2 leading-5 text-gray-700 transition-colors duration-150 border border-gray-300 rounded-lg focus:outline-none">取消</button>
          <button type="submit" @click="submitForm" class="px-4 py-2 leading-5 text-white transition-colors duration-150 bg-blue-600 border border-transparent rounded-lg active:bg-blue-600 hover:bg-blue-700 focus:outline-none">保存</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from "../axios";

// Props 定义
const props = defineProps({
  selectedUser: {
    type: Object,
    default: () => ({
      id: null,
      username: '',
      email: '',
      membership_level_id: null,
      balance: 0,
      commission: 0,
      referral_code: '',
      is_agent: false,
      is_active: true
    })
  },
  membershipLevels: {
    type: Array,
    default: () => []
  }
});

// Emit 定义
const emit = defineEmits(['update:showEditModal', 'user-updated']);

// Methods
const closeModal = () => {
  emit('update:showEditModal', false);
};

const submitForm = async () => {
  try {
    const response = await axios.put(`/api/v1/users/${props.selectedUser.id}`, props.selectedUser);
    closeModal();
    emit('user-updated', response.data);
  } catch (error) {
  }
};
</script>

