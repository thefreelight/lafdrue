<template>
  <div class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" v-show="showModal">
    <div class="relative top-1/4 mx-auto p-5 border w-1/3 shadow-lg rounded-md bg-white">
      <div class="mt-3 text-center">
        <h3 class="text-lg leading-6 font-medium text-gray-900" v-text="title"></h3>
        <div class="mt-2 px-7 py-3">
          <p class="text-sm text-gray-500" v-text="message"></p>
        </div>
        <div class="flex items-center justify-center px-4 py-3 space-x-3"> <!-- Flex container -->
          <button id="delete-btn" @click="confirmAction" class="px-4 py-2 bg-red-500 text-white text-base font-medium rounded-md shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 flex-1"> <!-- Flex child -->
            确认删除
          </button>
          <button id="cancel-btn" @click="closeModal" class="px-4 py-2 bg-white text-base font-medium rounded-md shadow-sm hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 flex-1"> <!-- Flex child -->
            取消
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>

const props = defineProps({
  showModal: Boolean,
  title: String,
  message: String,
  action: Function
});

const emit = defineEmits(['update:showModal']);

const closeModal = () => {
  emit('update:showModal', false);
};

const confirmAction = () => {
  props.action();
  closeModal();
};
</script>
