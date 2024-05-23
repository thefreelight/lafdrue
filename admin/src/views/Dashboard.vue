<template>
  <div class="p-8 space-y-4">
    <h1 class="text-2xl font-semibold text-gray-800">仪表盘概览</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-indigo-500 p-4 rounded-md">
            <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M..."/>
            </svg>
          </div>
          <div class="ml-4">
            <div class="text-lg leading-6 font-medium text-gray-900">用户总数</div>
            <div class="text-lg leading-6 font-semibold text-gray-900">123</div>
          </div>
        </div>
      </div>
      <!-- 更多统计卡片 -->
    </div>
  </div>
</template>


<script>
export default {
  name: 'Dashboard',
  // 这里可以添加获取数据的逻辑
};
</script>
