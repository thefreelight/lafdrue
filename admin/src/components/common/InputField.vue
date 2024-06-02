<template>
  <div>
    <component
        :is="input.component || 'input'"
        v-model="modelValue"
        v-bind="input.options"
        :type="input.type"
        :id="input.model"
        :placeholder="input.placeholder"
        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  input: {
    type: Object,
    required: true,
  },
  modelValue: {
    type: [String, Number, Boolean, Array, Object],
    default: '',
  },
});

const emit = defineEmits(['update:modelValue']);

const updateValue = (value) => {
  if (props.input.type === 'number') {
    const numberValue = value === '' ? null : parseFloat(value);
    emit('update:modelValue', numberValue);
  } else {
    emit('update:modelValue', value);
  }
};

const modelValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});
</script>
