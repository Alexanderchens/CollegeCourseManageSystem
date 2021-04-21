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

Vue.use(ElementUI)
Vue.use(VueResource)
// import axios from 'axios'
//
// axios.defaults.baseUrl = 'http://127.0.0.1:8888/api/private/v1/'
// Vue.prototype.$http = axios
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
