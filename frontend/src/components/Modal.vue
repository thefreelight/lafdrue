<template>
  <div v-if="isVisible" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
    <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
      <div class="mt-3 text-center">
        <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100">
          <!-- 可以放置图标 -->
        </div>
        <h3 class="text-lg leading-6 font-medium text-gray-900">{{ message }}</h3>
        <div class="mt-5 sm:mt-6">
          <button @click="close" class="text-white bg-blue-500 border-0 py-2 px-6 focus:outline-none hover:bg-blue-600 rounded">
            确定
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isVisible: Boolean,
    message: String
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
};
</script>
