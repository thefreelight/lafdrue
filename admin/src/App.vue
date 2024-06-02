<template>
  <n-message-provider>
    <div class="min-h-screen flex flex-col">
      <header class="bg-gray-800 text-white py-4 px-6 flex justify-between items-center">
        <h1 class="text-xl font-semibold">LAFDRUE后台管理系统</h1>
        <nav>
          <button @click="logout" class="text-gray-200 hover:text-gray-400 flex items-center">
            <font-awesome-icon icon="sign-out-alt" class="mr-2" /> 退出
          </button>
        </nav>
      </header>
      <div class="flex flex-1">
        <Sidebar />
        <main class="flex-1 p-6 overflow-auto">
          <router-view></router-view>
        </main>
      </div>
    </div>
  </n-message-provider>
</template>

<script setup>
import Sidebar from './components/layout/Sidebar.vue'
import { useRouter } from 'vue-router'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSignOutAlt } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'

library.add(faSignOutAlt)

const router = useRouter()

function logout() {
  localStorage.removeItem('access_token')
  router.push('/login')
}
</script>
