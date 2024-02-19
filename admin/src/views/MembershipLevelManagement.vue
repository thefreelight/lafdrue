<template>
  <div class="container mx-auto p-6">
    <div class="mb-6">
      <button @click="showAddModal = true" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        添加会员等级
      </button>
    </div>

    <ListTable :headers="membershipLevelHeaders" :items="membershipLevels">
      <template #actions="{ item }">
        <button @click="editMembershipLevel(item)" class="text-indigo-600 hover:text-indigo-900 mr-2">
          编辑
        </button>
        <button @click="openDeleteConfirmation(item)" class="text-red-600 hover:text-red-900">
          删除
        </button>
      </template>
    </ListTable>

    <!-- 使用 FormModal 组件来添加和编辑会员等级 -->
    <FormModal
        v-if="showAddModal || showEditModal"
        :title="showAddModal ? '添加会员等级' : '编辑会员等级'"
        :inputs="membershipLevelFormConfig"
        :model="selectedLevel"
        :onSave="handleSaveMembershipLevel"
        :onClose="closeModal"
    />

    <DeleteConfirmationModal
        v-if="showDeleteConfirmation"
        :showModal="showDeleteConfirmation"
        title="删除会员等级"
        message="您确定要删除这个会员等级吗？此操作不能撤销。"
        :action="deleteMembershipLevel"
        @update:showModal="handleModalClose"
    />

  </div>
</template>

<script setup>
import {ref, onMounted, reactive} from 'vue';
import ListTable from '../components/ListTable.vue';
import FormModal from "../components/FormModal.vue";
import DeleteConfirmationModal from '../components/DeleteConfirmationModal.vue';
import axios from '../axios';

const membershipLevels = ref([]);
const showEditModal = ref(false);
const showAddModal = ref(false);
const showDeleteConfirmation = ref(false);

const membershipLevelHeaders = [
  {text: 'ID', value: 'id'},
  {text: '名称', value: 'name'},
  {text: '优惠', value: 'benefits'},
  {text: '所需积分', value: 'points_required'},
  {text: '折扣', value: 'discount'},
  {text: '操作', value: 'actions'},
];

// 状态变量
const selectedLevel = reactive({
  id: '',
  name: '',
  benefits: '',
  points_required: '',
  discount: ''
});

// 表单配置
const membershipLevelFormConfig = [
  {
    label: '名称',
    model: 'name',
    type: 'text',
    placeholder: '请输入会员等级名称',
  },
  {
    label: '优惠',
    model: 'benefits',
    type: 'text',
    placeholder: '请输入会员等级优惠',
  },
  {
    label: '所需积分',
    model: 'points_required',
    type: 'number',
    placeholder: '请输入所需积分',
  },
  {
    label: '折扣',
    model: 'discount',
    type: 'number',
    placeholder: '请输入折扣',
  }
];

// 方法定义
const handleSaveMembershipLevel = async (levelData) => {
  if (!levelData.name || !levelData.benefits || levelData.points_required === undefined || levelData.discount === undefined) {
    console.error("Please fill all the fields.");
    return;
  }

  try {
    let response;
    if (showAddModal.value) {
      // 如果 showAddModal 为 true，调用添加会员等级的接口
      response = await axios.post('/api/v1/membership_levels/', levelData);
      console.log("Membership level added:", response.data);
    } else if (selectedLevel.value && selectedLevel.value.id) {
      // 如果 selectedLevel 存在且包含 id，调用更新会员等级的接口
      response = await axios.put(`/api/v1/membership_levels/${selectedLevel.value.id}`, levelData);
      console.log("Membership level updated:", response.data);
    }

    // 保存成功后关闭模态框并刷新列表
    closeModal();
    await fetchMembershipLevels();
  } catch (error) {
    console.error("Error saving membership level:", error.response ? error.response.data : error);
  }
};


const fetchMembershipLevels = async () => {
  try {
    const response = await axios.get('/api/v1/membership_levels/');
    membershipLevels.value = response.data.items;
  } catch (error) {
    console.error("Failed to fetch membership levels:", error);
  }
};

const editMembershipLevel = (level) => {
  selectedLevel.value = level;
  showEditModal.value = true;
};

const openDeleteConfirmation = (level) => {
  // 设置当前选中的会员等级对象
  selectedLevel.value = level;
  // 显示删除确认模态框
  showDeleteConfirmation.value = true;
};


const deleteMembershipLevel = async () => {
  try {
    await axios.delete(`/api/v1/membership_levels/${selectedLevel.value.id}`);
    // 成功删除后刷新列表
    await fetchMembershipLevels();
    // 关闭删除确认模态框
    showDeleteConfirmation.value = false;
  } catch (error) {
    console.error("Failed to delete membership level:", error);
    // 出错时也应关闭模态框，或者根据需求显示错误消息
    showDeleteConfirmation.value = false;
  }
};



const closeModal = () => {
  showEditModal.value = false;
  showAddModal.value = false;
  showDeleteConfirmation.value = false;
  selectedLevel.value = null;
};

onMounted(fetchMembershipLevels);
</script>
