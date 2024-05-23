<template>
  <div>
    <!-- 文本或邮箱或密码输入 -->
    <input
      v-if="['text', 'email', 'password', 'number'].includes(input.type)"
      :type="input.type"
      :id="input.model"
      :placeholder="input.placeholder"
      :value="modelValue"
      @input="updateValue($event.target.value)"
      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
    />

    <!-- 文本区域输入 -->
    <textarea
      v-else-if="input.type === 'textarea'"
      :id="input.model"
      :placeholder="input.placeholder"
      :value="modelValue"
      @input="updateValue($event.target.value)"
      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
    ></textarea>

    <!-- 下拉选择框 -->
    <select
      v-else-if="input.type === 'select'"
      :id="input.model"
      v-model="modelValue"
      class="mt-1 block w-full border-gray-300 bg-white rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
    >
      <option v-for="option in input.options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>

    <!-- 复选框 -->
    <div v-else-if="input.type === 'checkbox'" class="flex items-center mt-2">
      <input
        type="checkbox"
        :id="input.model"
        v-model="modelValue"
        class="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
      >
      <label :for="input.model" class="ml-2 block text-sm text-gray-900">
        {{ input.label }}
      </label>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  input: {
    type: Object,
    required: true
  },
  modelValue: {
    type: [String, Number, Boolean, Array, Object],
    default: ''
  }
});

const emit = defineEmits(['update:modelValue']);

// 更新值的方法，根据输入类型转换值
const updateValue = (value) => {
  if (props.input.type === 'number') {
    // 将字符串转换为数字
    const numberValue = value === '' ? null : parseFloat(value);
    emit('update:modelValue', numberValue);
  } else {
    emit('update:modelValue', value);
  }
};

// 使用计算属性来处理 v-model
const modelValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});
</script>