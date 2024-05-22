<template>
  <n-message-provider>
    <Navbar />
    <router-view />
  </n-message-provider>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>
