<template>
  <div class="flex items-center justify-between gap-4 p-4 bg-white shadow-md rounded-lg">
    <!-- 左侧查询字段容器 -->
    <div class="flex flex-wrap gap-4">
      <div v-for="field in fields" :key="field.model" class="min-w-[120px] max-w-[200px]">
        <label :for="field.model" class="text-sm font-semibold text-gray-700">{{ field.label }}</label>
        <input
          v-if="field.type === 'text'"
          :type="field.type"
          :placeholder="field.placeholder"
          class="mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50 w-full"
          v-model="searchQuery[field.model]"
        />
        <select
          v-else-if="field.type === 'select'"
          class="mt-1 p-2 border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50 w-full"
          v-model="searchQuery[field.model]"
        >
          <option v-for="option in field.options" :key="option.value" :value="option.value">
            {{ option.text }}
          </option>
        </select>
      </div>
    </div>
    <!-- 右侧查询按钮 -->
    <button
      @click="submitSearch"
      class="ml-auto bg-blue-500 text-white px-6 py-2 rounded-md shadow-sm hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200 focus:ring-opacity-50"
    >
      查询
    </button>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';

const props = defineProps({
  fields: {
    type: Array,
    default: () => []
  }
});

// 创建一个响应式对象，用于存储搜索条件
const searchQuery = reactive(
  props.fields.reduce((acc, field) => {
    acc[field.model] = '';
    return acc;
  }, {})
);

const emit = defineEmits(['search']);

// 提交搜索，触发父组件的搜索事件
const submitSearch = () => {
  emit('search', searchQuery);
};
</script>
