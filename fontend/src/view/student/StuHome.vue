<template>
  <el-container class="home-container">
<!--    头部-->
    <el-header>
      <div>
        <img src="../../assets/logo.png" alt="" class="logo_pic">
        <span>选课管理系统-学生端</span>
      </div>
      <el-dropdown>
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>注销</el-dropdown-item>
          <el-dropdown-item divided>其他业务1</el-dropdown-item>
          <el-dropdown-item>其他业务2</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-header>
<!--    主体-->
    <el-container>
<!--      Aside-->
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
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-message"></i>
              <span>教务信息</span>
            </template>
            <el-menu-item-group>
              <el-menu-item :index="'/message'"><i class="el-icon-chat-line-square"></i>消息</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-collection"></i>
              <span>课程查询</span>
            </template>
            <el-menu-item-group>
              <el-menu-item :index="'/table'"> <i class="el-icon-s-grid"></i>学生课表</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group>
              <el-menu-item :index="'/query'"><i class="el-icon-info"></i>选课情况查询</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item :index="'/select'">
            <i class="el-icon-document"></i>
            <span slot="title">学生选课</span>
          </el-menu-item>
          <el-menu-item :index="'/classroom'">
            <i class="el-icon-question"></i>
            <span slot="title">查询空教室</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-container>
<!--        Main-->
        <el-main>
          <router-view></router-view>
        </el-main>
<!--        Footer-->
        <el-footer>
          <div>
            <p class="comment">Copyright © 2021 数据库实训小组.</p>
          </div>
        </el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      isCollapse: false
    }
  }
}
</script>

<style lang="less" scoped>
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
