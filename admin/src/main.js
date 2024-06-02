import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import naive from 'naive-ui'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret, faSignOutAlt, faTachometerAlt, faUsers, faChevronDown, faHandshake, faFileAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// 添加图标到库
library.add(faUserSecret, faSignOutAlt, faTachometerAlt, faUsers, faChevronDown, faHandshake, faFileAlt)

const app = createApp(App)

// 全局注册图标组件
app.component('font-awesome-icon', FontAwesomeIcon)

// 使用 naive-ui
app.use(naive)

// 使用路由
app.use(router)

app.mount('#app')
