<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-gray-800 text-white py-4 px-6 flex justify-between items-center">
      <h1 class="text-xl font-semibold">LAFDRUE后台管理系统</h1>
      <nav>
        <button @click="logout" class="text-gray-200 hover:text-gray-400">
          <font-awesome-icon icon="sign-out-alt" /> 退出
        </button>
      </nav>
    </header>
    <div class="flex flex-1">
      <aside class="bg-gray-700 p-4 w-64 space-y-2">
        <div v-for="item in navigation" :key="item.text" class="group">
          <div
            @click="item.children ? toggle(item) : navigateTo(item.path)"
            class="flex items-center text-gray-200 hover:text-white hover:bg-gray-600 p-2 rounded cursor-pointer"
          >
            <font-awesome-icon :icon="[item.iconPrefix, item.iconName]" class="mr-3" />
            {{ item.text }}
            <font-awesome-icon v-if="item.children" icon="chevron-down" class="ml-auto transition-transform" :class="{ 'rotate-180': item.isOpen }" />
          </div>
          <div v-if="item.isOpen" class="pl-4">
            <router-link
              v-for="subItem in item.children"
              :key="subItem.text"
              :to="subItem.path"
              class="block text-gray-200 hover:text-white hover:bg-gray-600 p-2 rounded"
            >
              {{ subItem.text }}
            </router-link>
          </div>
        </div>
      </aside>
      <main class="flex-1 p-6 overflow-auto">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSignOutAlt, faTachometerAlt, faUsers, faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { useRouter } from 'vue-router'

library.add(faSignOutAlt, faTachometerAlt, faUsers, faChevronDown)

export default {
  name: 'AppLayout',
  components: {
    FontAwesomeIcon
  },
  data() {
    return {
      navigation: [
        { path: '/dashboard', text: '仪表盘', iconName: 'tachometer-alt', iconPrefix: 'fas', isOpen: false },
        {
          path: '/users',
          text: '用户管理',
          iconName: 'users',
          iconPrefix: 'fas',
          isOpen: false,
          children: [
            { path: '/users/', text: '管理用户' },
            { path: '/users/levels', text: '会员等级' }
            // 更多子菜单项...
          ]
        },
        // 其他导航项...
      ]
    }
  },
  methods: {
    toggle(item) {
      item.isOpen = !item.isOpen
    },
    navigateTo(path) {
      this.$router.push(path);
    },
    logout() {
      localStorage.removeItem('access_token')
      window.location.href = '/login';
    }
  }
}
</script>

<style>
/* 添加旋转效果的样式 */
.rotate-180 {
  transform: rotate(180deg);
}
</style>
