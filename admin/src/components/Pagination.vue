<template>
  <div class="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6">
    <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
      <div>
        <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm" aria-label="分页">
          <button
              @click="changePage(currentPage - 1)"
              class="relative inline-flex items-center rounded-l-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-50"
              :class="{ 'cursor-not-allowed opacity-50': currentPage <= 1 }"
              :disabled="currentPage <= 1"
          >
            上一页
          </button>
          <button
              v-for="page in pages"
              :key="page"
              @click="changePage(page)"
              class="relative inline-flex items-center px-4 py-2 text-sm font-medium border"
              :class="{
    'border-gray-300 bg-indigo-600 text-white': page === currentPage,
    'border-gray-300 hover:bg-gray-100 text-gray-700 bg-white': page !== currentPage,
  }"
          >
            {{ page }}
          </button>

          <button
              @click="changePage(currentPage + 1)"
              class="relative inline-flex items-center rounded-r-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-50"
              :class="{ 'cursor-not-allowed opacity-50': currentPage >= totalPages }"
              :disabled="currentPage >= totalPages"
          >
            下一页
          </button>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import {computed} from 'vue';

const props = defineProps({
  currentPage: Number,
  totalPages: Number
});

const emit = defineEmits(['page-changed']);

const pages = computed(() => {
  const range = [];
  for (let i = 1; i <= props.totalPages; i++) {
    range.push(i);
  }
  return range;
});

const changePage = (newPage) => {
  if (newPage >= 1 && newPage <= props.totalPages) {
    emit('page-changed', newPage);
  }
};
</script>

<style scoped>
/* Your styles here */
</style>
