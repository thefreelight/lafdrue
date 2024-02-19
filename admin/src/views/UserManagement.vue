<template>
  <div class="container mx-auto p-6">
    <SearchComponent :fields="searchFields" @search="handleSearch"/>
    <ListTable :headers="userHeaders" :items="users">
      <template v-slot:email="{ item }">
        {{ item.email }}
      </template>
      <template v-slot:balance="{ item }">
        {{ item.balance.toFixed(2) }}
      </template>
      <template v-slot:is_agent="{ item }">
        {{ item.is_agent ? '是' : '否' }}
      </template>
      <template v-slot:commission="{ item }">
        {{ item.commission.toFixed(2) }}
      </template>
      <template v-slot:referral_code="{ item }">
        {{ item.referral_code }}
      </template>
      <template v-slot:is_active="{ item }">
        {{ item.is_active ? '是' : '否' }}
      </template>
      <template v-slot:actions="{ item }">
        <button @click="rechargeUser(item.id)" class="text-green-600 hover:text-green-900 mr-4">
          充值
        </button>
        <button @click="editUser(item)" class="text-indigo-600 hover:text-indigo-900">
          编辑
        </button>
        <button @click="openDeleteConfirmation(item.id)" class="text-red-600 hover:text-red-900 ml-4">
          删除
        </button>
      </template>
    </ListTable>
  </div>
  <FormModal
      v-if="showEditUserModal"
      :title="'编辑用户'"
      :inputs="userFormConfig"
      :model="selectedUser"
      :onSave="handleSaveUser"
      :onClose="handleCloseModal"
  />
  <!-- 使用 FormModal 组件处理充值操作 -->
    <FormModal
      v-if="showRechargeModal"
      :title="'用户充值'"
      :inputs="rechargeInputs"
      :model="rechargeModel"
      :onSave="handleRechargeSave"
      :onClose="handleRechargeClose"
    />
  <DeleteConfirmationModal
      v-if="showDeleteConfirmation"
      :showModal="showDeleteConfirmation"
      title="删除用户"
      message="您确定要删除这个用户吗？此操作不能撤销。"
      :action="deleteUser"
      @update:showModal="showDeleteConfirmation = $event"
  />

  <!-- 分页组件 -->
  <Pagination
      :current-page="currentPage"
      :total-pages="totalPages"
      @page-changed="handlePageChange"
  />


</template>


<script setup>
import axios from '../axios';
import {ref, computed, watch, onMounted, reactive} from 'vue';
import ListTable from '../components/ListTable.vue';
import DeleteConfirmationModal from '../components/DeleteConfirmationModal.vue';
import Pagination from '../components/Pagination.vue';
import FormModal from '../components/FormModal.vue';
import SearchComponent from '../components/SearchComponent.vue';


const users = ref([]);
const showEditUserModal = ref(false);
const showRechargeModal = ref(false);
const showDeleteConfirmation = ref(false);
const selectedUser = ref({});
const selectedUserId = ref(null);
const selectedId = ref(null);
const currentPage = ref(1);
const totalPages = ref(0);
const pageSize = ref(10);  // 假设你的每页大小是10
const membershipLevels = ref([]);


const userHeaders = [
  {text: 'ID', value: 'id'},
  {text: '用户名', value: 'username'},
  {text: '电子邮件', value: 'email'},
  {text: '会员等级', value: 'membership_level'},
  {text: '是否代理', value: 'is_agent'},
  {text: '余额', value: 'balance'},
  {text: '佣金', value: 'commission'},
  {text: '推荐码', value: 'referral_code'},
  {text: '是否激活', value: 'is_active'},
  {text: '操作', value: 'actions'},
];

const userFormConfig = ref([
  {
    label: '用户名',
    model: 'username',
    type: 'text',
    placeholder: '请输入用户名',
  },
  {
    label: '密码',
    model: 'password',
    type: 'password',
    placeholder: '请输入密码',
  },
  {
    label: '邮箱',
    model: 'email',
    type: 'email',
    placeholder: '请输入邮箱',
  },
  {
    label: '会员等级',
    model: 'membership_level_id',
    type: 'select',
    options: () => membershipLevels.value, // 假设membershipLevels是响应式的会员等级列表
  },
  {
    label: '推荐码',
    model: 'referral_code',
    type: 'text',
    placeholder: '请输入推荐码',
  },
  {
    label: '是否代理',
    model: 'is_agent',
    type: 'checkbox',
  },
  {
    label: '是否激活',
    model: 'is_active',
    type: 'checkbox',
  }
]);

// 初始化搜索字段
const searchFields = ref([
  {
    label: 'ID',
    model: 'id',
    type: 'text',
    placeholder: '搜索 ID...'
  },
  {
    label: '用户名',
    model: 'username',
    type: 'text',
    placeholder: '搜索用户名...'
  },
  {
    label: '电子邮件',
    model: 'email',
    type: 'text',
    placeholder: '搜索电子邮件...'
  },
  {
    label: '会员等级',
    model: 'membershipLevel',
    type: 'select',
    options: [
      {value: '', text: '所有等级'}
      // 更多等级将在组件加载时动态添加
    ],
    placeholder: '选择会员等级...'
  },
  {
    label: '是否代理',
    model: 'is_agent',
    type: 'select',
    options: [
      {value: '', text: '所有状态'},
      {value: 'true', text: '是'},
      {value: 'false', text: '否'}
    ],
    placeholder: '选择是否代理...'
  },
  {
    label: '余额',
    model: 'balance',
    type: 'text',
    placeholder: '搜索余额...'
  },
  {
    label: '佣金',
    model: 'commission',
    type: 'text',
    placeholder: '搜索佣金...'
  },
  {
    label: '推荐码',
    model: 'referralCode',
    type: 'text',
    placeholder: '搜索推荐码...'
  },
  {
    label: '是否激活',
    model: 'is_active',
    type: 'select',
    options: [
      {value: '', text: '所有状态'},
      {value: 'true', text: '是'},
      {value: 'false', text: '否'}
    ],
    placeholder: '选择是否激活...'
  }
]);

const filters = reactive({
  id: '', // 用户ID
  username: '', // 用户名
  email: '', // 电子邮件
  membershipLevel: '', // 会员等级
  is_agent: '', // 是否代理
  balance: '', // 余额
  commission: '', // 佣金
  referralCode: '', // 推荐码
  is_active: '' // 是否激活
});

// 处理搜索事件
const handleSearch = (searchQuery) => {

  Object.assign(filters, searchQuery);
  // 重置当前页面为第一页，因为新的搜索可能有不同的分页数据
  currentPage.value = 1;

  fetchUsers(); // 调用 fetchUsers 函数，并传入新的搜索条件
};

watch(membershipLevels, (newLevels) => {
  const membershipLevelField = searchFields.value.find(field => field.model === 'membershipLevel');
  if (membershipLevelField) {
    membershipLevelField.options = [
      {value: '', text: '所有等级'},
      ...newLevels.map(level => ({value: level.id, text: level.name}))
    ];
  }
});
// 在组件加载时获取会员等级
const fetchMembershipLevels = async () => {
  try {
    const response = await axios.get('/api/v1/membership_levels/');
    if (response.data && Array.isArray(response.data)) {
      const membershipLevelField = searchFields.value.find(field => field.model === 'membershipLevel');
      membershipLevelField.options.push(...response.data.map(level => ({
        value: level.id, // 或者是level.name，取决于你的API返回的是哪个属性
        text: level.name
      })));
    }
  } catch (error) {
    console.error('获取会员等级失败:', error);
  }
};

onMounted(fetchMembershipLevels);


// 处理保存用户
// 在 handleSaveUser 函数中，如果保存成功，调用 fetchUsers 来刷新列表
const handleSaveUser = async (formData) => {
  try {
    const response = await axios.put(`/api/v1/users/${formData.id}`, formData);
    // 如果保存成功，重新获取用户列表
    if (response.status === 200) {
      await fetchUsers();
      showEditUserModal.value = false;
    }
  } catch (error) {
    console.error("保存用户失败:", error);
  }
};


// 关闭模态框
const handleCloseModal = () => {
  showEditUserModal.value = false;
};

const params = computed(() => ({
  ...filters,
  page: currentPage.value,
  size: pageSize.value
}));

// 更新 fetchUsers 函数以存储分页信息
const fetchUsers = async () => {
  try {
    // 创建一个新的对象，只包含非空的筛选条件
    const validParams = Object.entries(params.value).reduce((acc, [key, value]) => {
      // 如果值不是空字符串，则包含此参数
      if (value !== '') {
        acc[key] = value;
      }
      return acc;
    }, {});

    const response = await axios.get('/api/v1/users/', {
      params: validParams // 使用经过过滤的参数进行请求
    });
    users.value = response.data.items;
    totalPages.value = response.data.pages;
  } catch (error) {
    console.error('There was an error fetching the users:', error);
  }
};


const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchUsers();
};


// 监听筛选条件变化并重新获取用户列表
watch(filters, fetchUsers, {deep: true});

watch(currentPage, fetchUsers); // This watcher will call fetchUsers whenever currentPage changes


// 删除用户
const deleteUser = async () => {
  try {
    const response = await axios.delete(`/api/v1/users/${selectedId.value}`);
    console.log(`用户删除成功: ${response.data.detail}`);
    showDeleteConfirmation.value = false;
    fetchUsers();
  } catch (error) {
    console.error(`删除用户失败: ${error}`);
  }
};

// 打开编辑模态框
const editUser = (user) => {
  selectedUser.value = user;
  showEditUserModal.value = true;
};


// 定义用户充值的模型和输入配置
const rechargeModel = reactive({
  balance: 0,
  commission: 0,
});

const rechargeInputs = ref([
  {
    label: '余额充值',
    model: 'balance',
    type: 'number',
    placeholder: '请输入充值的余额'
  },
  {
    label: '佣金充值',
    model: 'commission',
    type: 'number',
    placeholder: '请输入充值的佣金'
  }
]);


// 定义打开充值模态框的方法
const rechargeUser = (userId) => {
  // 设置选中的用户ID
  selectedUserId.value = userId;
  // 显示充值模态框
  showRechargeModal.value = true;
};



// 处理充值保存事件
const handleRechargeSave = async (formData) => {
  try {
    const response = await axios.post('/api/v1/recharge/', {
      user_id: selectedUserId.value,
      balance: formData.balance,
      commission: formData.commission
    });
    showRechargeModal.value = false;
    // 这里可以发出一个事件，通知父组件充值成功
    fetchUsers()
  } catch (error) {
    console.error('Recharge failed:', error);
  }
};

// 处理充值模态框关闭事件
const handleRechargeClose = () => {
  showRechargeModal.value = false;
};

// 打开删除确认模态框
const openDeleteConfirmation = (id) => {
  selectedId.value = id;
  showDeleteConfirmation.value = true;
};

// 页面加载时获取用户数据
onMounted(fetchUsers);

</script>

<style scoped>
/* 可以在此处添加特定的CSS样式 */
</style>

