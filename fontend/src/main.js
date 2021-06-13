import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/css/global.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import VueResource from 'vue-resource'
import cors from 'cors'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.prototype.axios = axios

Vue.use(ElementUI)
Vue.use(VueResource)
// Vue.use(cors())
// import axios from 'axios'
//
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
axios.defaults.baseURL = 'http://127.0.0.1:5000'
// Vue.prototype.$http = axios
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
