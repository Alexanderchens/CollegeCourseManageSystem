import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './view/Login/Login'
import Home from './view/student/StuHome'
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/login',
      component: Login
    },
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/student',
      component: Home
    }
  ]
})

// // 挂载路由导航
// router.beforeEach((to, from, next) => {
//   // to将要访问的路径
//   // from从哪里跳转
//   // next 函数
//   // 放行
//   if (to.path === '/login') return next()
//   const tokenStr = window.sessionStorage.getItem('token')
//   if (!tokenStr) return next('/login')
//   next()
// })

export default router
