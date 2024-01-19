<template>
  <div class="container">
    <input v-model="email" @blur="validateEmail" placeholder="邮箱" />
    <span v-if="emailError">{{ emailError }}</span>
    <!-- 其他注册表单字段 -->
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      email: '',
      emailError: ''
    };
  },
  methods: {
    validateEmail() {
      if (!this.email.includes('@')) {
        this.emailError = '请输入有效的邮箱地址。';
      } else {
        this.emailError = '';
      }
    }
  }
}
</script>
