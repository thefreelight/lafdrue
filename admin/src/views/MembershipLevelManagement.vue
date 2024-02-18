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

    <MembershipLevelModal v-if="showEditModal || showAddModal" :selectedLevel="selectedLevel" @close="closeModal" @refresh="fetchMembershipLevels" />
    <DeleteConfirmationModal v-if="showDeleteConfirmation" :selectedItem="selectedLevel" @close="closeModal" @confirm="deleteMembershipLevel" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import ListTable from '@/components/ListTable.vue';
import MembershipLevelModal from '@/components/MembershipLevelModal.vue';
import DeleteConfirmationModal from '@/components/DeleteConfirmationModal.vue';
import axios from 'axios';

const membershipLevels = ref([]);
const showEditModal = ref(false);
const showAddModal = ref(false);
const showDeleteConfirmation = ref(false);
const selectedLevel = ref(null);

const membershipLevelHeaders = [
  { text: 'ID', value: 'id' },
  { text: '名称', value: 'name' },
  { text: '优惠', value: 'benefits' },
  { text: '所需积分', value: 'points_required' },
  { text: '折扣', value: 'discount' },
  { text: '操作', value: 'actions' },
];

const fetchMembershipLevels = async () => {
  try {
    const response = await axios.get('/api/membership-levels');
    membershipLevels.value = response.data;
  } catch (error) {
    console.error("Failed to fetch membership levels:", error);
  }
};

const editMembershipLevel = (level) => {
  selectedLevel.value = level;
  showEditModal.value = true;
};

const openDeleteConfirmation = (level) => {
  selectedLevel.value = level;
  showDeleteConfirmation.value = true;
};

const deleteMembershipLevel = async () => {
  try {
    await axios.delete(`/api/membership-levels/${selectedLevel.value.id}`);
    fetchMembershipLevels();
    closeModal();
  } catch (error) {
    console.error("Failed to delete membership level:", error);
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
