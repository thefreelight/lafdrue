<template>
  <div>
    <div class="welcome-section text-center p-10">
      <h1 class="text-4xl font-bold">欢迎来到Lafdrue</h1>
      <p class="text-xl mt-4">高效、稳定、快速的自动售货解决方案</p>
    </div>
    <div>
    <ProductList  />
  </div>
    <div class="features-section p-10">
      <div class="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- 特色产品或服务卡片 -->
      </div>
    </div>

    <div class="about-section bg-gray-100 p-10">
      <div class="container mx-auto text-center">
        <h2 class="text-3xl font-bold">关于我们</h2>
        <p class="mt-4">公司或团队介绍...</p>
      </div>
    </div>

    <div class="contact-section p-10">
      <div class="container mx-auto text-center">
        <h2 class="text-3xl font-bold">联系我们</h2>
        <p class="mt-4">联系方式或链接到联系页面</p>
      </div>
    </div>
  </div>
</template>

<script>
import ProductList from '../components/ProductList.vue';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Home',
  components: {
    ProductList
  }
};

</script>

<style>
/* 在这里添加您的 CSS 样式 */
</style>
