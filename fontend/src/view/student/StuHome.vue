<!--学生主页面框架-->
<template>
  <div class="app-wrapper">
    <el-container>
      <!--      侧边栏-->
      <el-aside width="200px">
        <el-menu
          :default-active="$route.path"
          class="el-menu-vertical-aside"
          @open="handleOpen"
          @close="handleClose"
          :collapse="isCollapse"
          background-color="#03152a"
          text-color="#fff"
          router
          @click="saveNavState('/')">
          <div class="side-container" :class="collapsed ? 'folded' : 'unfolded'">
            <div class="logo">
              <a href="/">
                <img src="../../assets/img/logo.png" alt="logo">
              </a>
            </div>
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-message"></i>
                <span>教务信息</span>
              </template>
              <el-menu-item-group>
                <el-menu-item :index="'/student/message'"><i class="el-icon-chat-line-square"></i>消息</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-collection"></i>
                <span>课程查询</span>
              </template>
              <el-menu-item-group>
                <el-menu-item :index="'/student/table'"> <i class="el-icon-s-grid"></i>学生课表</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group>
                <el-menu-item :index="'/student/query'"><i class="el-icon-info"></i>选课情况查询</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item :index="'/student/select'">
              <i class="el-icon-document"></i>
              <span slot="title">学生选课</span>
            </el-menu-item>
            <el-menu-item :index="'/student/classroom'">
              <i class="el-icon-question"></i>
              <span slot="title">查询空教室</span>
            </el-menu-item>
          </div>
        </el-menu>
      </el-aside>
      <el-container>
        <el-container class="home-container">
          <!--    头部-->
          <el-header>
            <div>
              <img src="../../assets/img/logo.png" alt="" class="logo_pic">
              <span>选课管理系统-学生端</span>
            </div>

<!--            右侧头像-->
            <el-dropdown class="user-avatar-wrapper" @command="handleCommand">
              <div class="avatar-box">
                <el-avatar size="small" src="data:image/png;base64,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" />
                <i class="el-icon-caret-bottom" />
              </div>
<!--              下拉菜单-->
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="userCenter">个人中心</el-dropdown-item>
                <el-dropdown-item command="loginOut">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-header>
          <!--    主体-->
          <el-main>
            <router-view></router-view>
          </el-main>
<!--          底部-->
          <el-footer>
            <div>
              <p class="comment">Copyright © 2021 数据库实训小组.</p>
            </div>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>

</template>

<script>
import Cookies from 'js-cookie'
const TokenKey = 'ADMIN_DESIGN_KEY'
export default {
  name: 'student',
  data () {
    return {
      isCollapse: false,  // 前端样式展现，塌陷回去（不用管）
      userId: '',  // 用户id
      userType: ''  // 用户类型
    }
  },
  // 页面初始化函数,获取Student的主键id
  created () {
    const user = JSON.parse(window.sessionStorage.getItem('user'))
    this.userId = user.username
    this.userType = user.userType
    console.log(this.userId)
  },
  methods: {
    /**
     * 处理点击头像后的时间
     */
    handleCommand(command) {
      // 退出登录
      if (command === 'loginOut') {
        this.loginOut()
      }
      // 个人中心
      if (command === 'userCenter') {
        const routeData = this.$router.resolve({
          name: 'userCenter',
          path: '/user-center',
          params: {
            userId: this.userId,
            type: this.userType
          }
        })
        window.open(routeData.href, '_blank')
      }
    },
    /**
     * 退出登录
     */
    loginOut() {
      this.$confirm('确定注销并退出系统吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.removeToken()
        this.$router.push('/login')
      })
    },
    removeToken() {
      return Cookies.remove(TokenKey)
    }
  }
}
</script>

<style lang="less" scoped>
/*头像*/
.user-avatar-wrapper {
  float: left;
  width: 48px;
  padding: 3px 0 3px 20px;
  margin-left: 20px;
  border-left: solid 1px #ddd;
  cursor: pointer;
  .avatar-box {
    outline: none;
  }
  .el-avatar--small {
    display: inline-block;
    vertical-align: middle;
    width: 32px;
    height: 32px;
    line-height: 32px;
  }
  i {
    display: inline-block;
    vertical-align: middle;
    margin-left: 2px;
  }
}
.logo {
  width: 80px;
  height: 64px;
  padding: 10px;
  box-sizing: border-box;
  img {
    display: block;
    width: 100%;
    height: 100%;
  }
}

.el-header{
  background-color: #f1f1f1;
  display: flex;
  justify-content: space-between;
}

  .el-aside{
    background-color: #03152a;
  }

  .el-main{
    background-color: #dddfe2;
    min-height: 1000px;
  }

  .home-container{
    height: 100%;
  }

  .logo_pic{
    height: 50px;
    width: 50px;
    border-radius: 50%;
  }

  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }

  .el-icon-arrow-down {
    font-size: 12px;
  }

  .el-menu-vertical-aside {
    border: none;
  }

  .el-menu-vertical-aside:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  .comment{
    height: 60px;
    line-height: 60px;
    text-align: left;
    font-size: 20px;
    color: #999999;
  }

</style>
