<template>
  <aside class="bg-gray-700 p-4 w-64 space-y-2">
    <div v-for="item in navigation" :key="item.text" class="group">
      <div
          @click="item.children ? toggle(item) : navigateTo(item.path)"
          class="flex items-center text-gray-200 hover:text-white hover:bg-gray-600 p-2 rounded cursor-pointer"
      >
        <font-awesome-icon :icon="[item.iconPrefix, item.iconName]" class="mr-3" />
        {{ item.text }}
        <font-awesome-icon v-if="item.children" icon="chevron-down" class="ml-auto transition-transform duration-300" :class="{ 'rotate-180': item.isOpen }" />
      </div>
      <div v-if="item.isOpen" class="pl-4 space-y-1">
        <router-link
            v-for="subItem in item.children"
            :key="subItem.text"
            :to="subItem.path"
            class="block text-gray-200 hover:text-white hover:bg-gray-600 p-2 rounded transition-colors duration-300"
        >
          {{ subItem.text }}
        </router-link>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'

library.add(faChevronDown)

const router = useRouter()

const navigation = ref([
  { path: '/dashboard', text: '仪表盘', iconName: 'tachometer-alt', iconPrefix: 'fas', isOpen: false },
  {
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
  {
    text: '交易管理',
    iconName: 'handshake',
    iconPrefix: 'fas',
    isOpen: false,
    children: [
      { path: '/category/', text: '商品分类' },
      { path: '/product/', text: '商品管理' },
      { path: '/card/', text: '卡密管理' },
      { path: '/order/', text: '订单管理' }
      // 可能的其他交易相关管理...
    ]
  },
  {
    text: '内容管理',
    iconName: 'file-alt',
    iconPrefix: 'fas',
    isOpen: false,
    children: [
      { path: '/articles', text: '文章管理' },
      { path: '/category', text: '分类管理' }
    ]
  }
])

function toggle(item) {
  item.isOpen = !item.isOpen
}

function navigateTo(path) {
  router.push(path)
}
</script>

<style scoped>
/* 添加旋转效果的样式 */
.rotate-180 {
  transform: rotate(180deg);
}
</style>
