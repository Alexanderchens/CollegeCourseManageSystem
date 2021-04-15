import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './view/Login/Login'
import Home from './view/student/StuHome'
import Message from './view/student/eduMessage/Message'
import NotFound from './view/page404'
import Table from './view/student/class/table'
import Query from './view/student/class/query'
import Select from './view/student/select/select'
import Classroom from './view/student/classroom/classroom'
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
      component: Home,
      redirect: '/message',
      children: [
        { path: '/message', component: Message },
        { path: '/table', component: Table },
        { path: '/query', component: Query },
        { path: '/select', component: Select },
        { path: '/classroom', component: Classroom }
      ]
    },
    {
      path: '/404',
      component: NotFound,
      name: '404',
      hidden: true,
      children: []
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
