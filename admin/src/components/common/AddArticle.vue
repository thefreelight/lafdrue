<template>
  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-8 max-w-2xl w-full">
      <h3 class="text-xl font-semibold mb-4">{{ title }}</h3>
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div>
          <label for="title" class="block text-gray-700 text-sm font-bold mb-2">标题</label>
          <input
              v-model="formData.title"
              id="title"
              type="text"
              placeholder="请输入文章标题"
              class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
          />
        </div>
        <div>
          <label for="content" class="block text-gray-700 text-sm font-bold mb-2">内容</label>
          <Toolbar
              :editor="editorRef"
              :defaultConfig="toolbarConfig"
              :mode="mode"
          />
          <Editor
              v-model="formData.content"
              :defaultConfig="editorConfig"
              :mode="mode"
              @onCreated="handleCreated"
              class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
              style="height: 400px;"
          />
        </div>
        <div>
          <label for="author" class="block text-gray-700 text-sm font-bold mb-2">作者</label>
          <input
              v-model="formData.author"
              id="author"
              type="text"
              placeholder="请输入作者名"
              class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
          />
        </div>
        <div>
          <label for="category" class="block text-gray-700 text-sm font-bold mb-2">分类</label>
          <select
              v-model="formData.category_id"
              id="category"
              class="mt-1 block w-full border-gray-300 bg-white rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          >
            <option v-for="category in categories" :key="category.value" :value="category.value">
              {{ category.text }}
            </option>
          </select>
        </div>
        <div>
          <label for="language" class="block text-gray-700 text-sm font-bold mb-2">语言</label>
          <input
              v-model="formData.language"
              id="language"
              type="text"
              placeholder="请输入语言代码"
              class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 sm:text-sm"
          />
        </div>
        <div class="flex justify-end pt-2">
          <button @click="closeModal" type="button"
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
import { ref, watch } from 'vue';
import { Editor, Toolbar } from '@wangeditor/editor-for-vue';
import '@wangeditor/editor/dist/css/style.css'; // 引入 css

const props = defineProps({
  title: String,
  model: Object,
  categories: Array,
  onSave: Function,
  onClose: Function,
});

const editorRef = ref(null);
const formData = ref({ ...props.model });
const toolbarConfig = {};
const editorConfig = {
  placeholder: '请输入内容...',
  MENU_CONF: {
    'video': {
      fieldName: 'video',
      maxFileSize: 50 * 1024 * 1024, // 50MB
      server: '/your_video_upload_url', // 视频上传接口地址
    },
  },
};
const mode = 'default';

const handleCreated = (editor) => {
  editorRef.value = Object.seal(editor); // 记录 editor 实例，重要！
};

const handleSubmit = () => {
  console.log('Form Data:', formData.value);
  props.onSave(formData.value);
};

const closeModal = () => {
  props.onClose();
};

watch(() => props.model, (newVal) => {
  formData.value = { ...newVal };
});
</script>

<style scoped>
/* 可以在此处添加特定的CSS样式 */
</style>
