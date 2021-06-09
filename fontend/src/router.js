import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './view/Login/Login'
import StuHome from './view/student/StuHome'
import Message from './view/student/eduMessage/Message'
import NotFound from './view/page404'
import Table from './view/student/class/table'
import Query from './view/student/class/query'
import Select from './view/student/select/select'
import Classroom from './view/student/classroom/classroom'
import AdminHome from './view/admin/adminHome'
import quillEditor from 'vue-quill-editor'
import Notification from './view/admin/note/notification'
import Verify from './view/admin/verify/verify'
import Administration from './view/admin/administration/administration'
import ConfirmForm from './view/admin/verify/confirm'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    // 登录
    {
      path: '/login',
      component: Login
    },
    {
      path: '/',
      redirect: '/login'
    },
    // 学生
    {
      path: '/student',
      name: 'student',
      component: StuHome,
      redirect: '/student/message',
      children: [
        { path: 'message', component: Message, name: 'message' },
        { path: 'table', component: Table },
        { path: 'query', component: Query },
        { path: 'select', component: Select },
        { path: 'classroom', component: Classroom }
      ]
    },
    // 课程详情页面
    {
      path: '/classInfo',
      component: () => import('./view/student/class/detailInfo')
    },
    // 管理员
    {
      path: '/admin',
      mode: 'history',
      component: AdminHome,
      redirect: '/admin/notification',
      children: [
        { path: 'notification', component: Notification },
        {
          path: 'verify',
          component: Verify
        },
        { path: 'edit', component: Administration }
      ]
    },
    {
      path: '/admin/application/:id',
      component: ConfirmForm
    },
    // 个人中心页
    {
      path: '/user-center',
      name: 'userCenter',
      component: () => import('./view/UserCenter')
    },
    {
      path: '/404',
      component: NotFound,
      name: '404',
      hidden: true
    }
  ],
  components: {
    quillEditor
  }
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
