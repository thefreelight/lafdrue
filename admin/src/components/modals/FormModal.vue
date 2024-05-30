<template>
  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-8 max-w-xl w-full">
      <h3 class="text-xl font-semibold mb-4">{{ title }}</h3>
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div v-for="(input, index) in inputs" :key="index">
          <label :for="input.model" class="block text-gray-700 text-sm font-bold mb-2">
            {{ input.label }}
          </label>
          <input-field :input="input" v-model="formData[input.model]"/>
        </div>
        <div class="flex justify-end pt-2">
          <button type="button" @click="closeModal"
                  class="mr-2 px-4 py-2 leading-5 text-gray-700 transition-colors duration-150 border border-gray-300 rounded-lg hover:bg-gray-100 focus:outline-none">
            取消
          </button>
          <button type="submit"
                  class="px-4 py-2 leading-5 text-white transition-colors duration-150 bg-blue-600 border border-transparent rounded-lg hover:bg-blue-700 focus:outline-none">
            保存
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import {ref, watch, toRefs} from 'vue';
import InputField from '../common/InputField.vue';

const props = defineProps({
  title: String,
  inputs: Array,
  model: Object,
  onSave: Function,
  onClose: Function,
  useVModel: {
    type: Boolean,
    default: false,
  },
});

// 解构props以方便使用
const { title, inputs, model, onSave, onClose, useVModel } = props;

const formData = ref({});

if (props.useVModel) {
  watch(
    () => props.modelValue,
    (newVal) => {
      formData.value = { ...newVal };
    },
    { immediate: true }
  );

  watch(formData, (newVal) => {
    emit('update:modelValue', newVal);
  }, { deep: true });
} else {
  watch(props.model, (newVal) => {
    formData.value = {...newVal};
  }, {immediate: true});
}



const closeModal = () => {
  onClose();
};

const handleSubmit = () => {
  onSave(formData.value);
};
</script>
