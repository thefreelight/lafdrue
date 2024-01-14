```vue
   <!-- LoginComponent.vue -->
   <template>
     <form @submit.prevent="login">
       <input v-model="username" type="text" placeholder="Username" />
       <input v-model="password" type="password" placeholder="Password" />
       <button type="submit">Login</button>
     </form>
   </template>

   <script>
   export default {
     data() {
       return {
         username: '',
         password: ''
       };
     },
     methods: {
       login() {
         // 实现登录逻辑
       }
     }
   };
   </script>