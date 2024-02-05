<template>
  <div class="container mx-auto p-6">
    <div class="mb-6 flex space-x-2">
      <!-- 查询框样式优化 -->
      <input
          type="text"
          v-model="filters.username"
          class="py-2 pl-3 pr-10 w-1/4 rounded-md border-2 border-gray-300 focus:outline-none focus:border-indigo-500"
          placeholder="用户名"
      />
      <input
          type="text"
          v-model="filters.email"
          class="py-2 pl-3 pr-10 w-1/4 rounded-md border-2 border-gray-300 focus:outline-none focus:border-indigo-500"
          placeholder="邮箱"
      />
      <!-- 代理状态选择 -->
      <select v-model="filters.isAgent"
              class="py-2 pl-3 pr-10 w-1/4 rounded-md border-2 border-gray-300 focus:outline-none focus:border-indigo-500">
        <option value="">代理状态</option>
        <option value="true">是</option>
        <option value="false">否</option>
      </select>
      <!-- 激活状态选择 -->
      <select v-model="filters.isActive"
              class="py-2 pl-3 pr-10 w-1/4 rounded-md border-2 border-gray-300 focus:outline-none focus:border-indigo-500">
        <option value="">激活状态</option>
        <option value="true">已激活</option>
        <option value="false">未激活</option>
      </select>
      <!-- 查询按钮 -->
      <button @click="applyFilters"
              class="py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none">
        查询
      </button>
    </div>

    <div class="bg-white shadow overflow-hidden rounded-md">
      <table class="min-w-full">
        <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            ID
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            用户名
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            会员等级
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            是否代理
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            电子邮件
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            余额
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            佣金
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            推荐码
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            是否激活
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            操作
          </th>
        </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="user in filteredUsers" :key="user.id">
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.id }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.username }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.membership_level?.name || '无' }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.is_agent ? '是' : '否' }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.email }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.balance.toFixed(2) }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.commission.toFixed(2) }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.referral_code }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            {{ user.is_active ? '是' : '否' }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button @click="rechargeUser(user.id)" class="text-green-600 hover:text-green-900 mr-4">
              充值
            </button>
            <button @click="editUser(user)" class="text-indigo-600 hover:text-indigo-900">
              编辑
            </button>
            <button @click="deleteUser(user.id)" class="text-red-600 hover:text-red-900 ml-4">
              删除
            </button>

          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
  <UserEditModal v-if="showEditModal" :selectedUser="selectedUser" @update:showEditModal="showEditModal = $event"/>
  <UserRechargeModal
  v-if="showRechargeModal"
  :selectedUserId="selectedUserId"
  :showRechargeModal="showRechargeModal"
  @update:showRechargeModal="showRechargeModal = $event"
/>


</template>

<script>
import axios from '../axios';
import {ref, computed} from 'vue';
import UserEditModal from '../components/UserEditModal.vue';
import UserRechargeModal from '../components/UserRechargeModal.vue';

export default {
  name: 'UserManagement',
  components: {
    UserEditModal,
    UserRechargeModal
  },
  setup() {
    const users = ref([]);
    const showEditModal = ref(false);
    const showRechargeModal = ref(false);
    const selectedUser = ref(null);
    const selectedUserId = ref(null);

    // 打开编辑模态框
    const editUser = (user) => {

      selectedUser.value = user;
      showEditModal.value = true;

    };

    // 打开充值模态框
    const rechargeUser = (userId) => {
      selectedUserId.value = userId;
      showRechargeModal.value = true;
    };

    // 添加筛选条件
    const filters = ref({
      username: '',
      email: '',
      isAgent: '',
      isActive: ''
    });

    // 获取用户数据
    const fetchUsers = async () => {
      try {
        // 假设API支持查询参数，我们可以将filters传递给API
        const response = await axios.get('/api/v1/users/', {params: filters.value});
        users.value = response.data;
      } catch (error) {
        console.error('There was an error fetching the users:', error);
      }
    };

    // 根据筛选条件计算过滤后的用户列表
    const filteredUsers = computed(() => {
      return users.value.filter(user => {
        return (
            (filters.value.username ? user.username.toLowerCase().includes(filters.value.username.toLowerCase()) : true) &&
            (filters.value.email ? user.email.toLowerCase().includes(filters.value.email.toLowerCase()) : true) &&
            (filters.value.isAgent !== '' ? user.is_agent.toString() === filters.value.isAgent : true) &&
            (filters.value.isActive !== '' ? user.is_active.toString() === filters.value.isActive : true)
        );
      });
    });


    // 监听筛选条件变化并重新获取用户列表
    const applyFilters = () => {
      fetchUsers();
    };

    // 删除用户
    const deleteUser = async (userId) => {
      try {
        await axios.delete(`/api/v1/users/${userId}`);
        fetchUsers(); // 删除后重新获取用户列表
      } catch (error) {
        console.error('There was an error deleting the user:', error);
      }
    };

    // 初始加载用户数据
    fetchUsers();

    return {
      filters,
      filteredUsers,
      applyFilters,
      editUser,
      rechargeUser,
      deleteUser,
      showEditModal,
      showRechargeModal,
      selectedUser,
      selectedUserId,
    };
  }
};
</script>

<style scoped>
/* 可以在此处添加特定的CSS样式 */
</style>
