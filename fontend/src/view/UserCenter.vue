<!--个人主页-->
<!--目前展示信息不多可以自行根据数据库字段补全-->
<template>
  <div class="background">
    <div class="user-center-wrapper">
      <el-card shadow="hover" :body-style="{padding: '50px'}">
        <div class="user-avatar">
          <img src="data:image/png;base64,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" alt="avatar">
        </div>
        <ul class="user-info">
<!--          这里可以根据数据库再开修改显示字段-->
          <li>
            <label>用户名：</label>
            <span>{{ userInfo.username }}</span>
          </li>
          <li>
            <label>角色：</label>
            <span>{{ userInfo.roles }}</span>
          </li>
          <li>
            <label>电话号码：</label>
            <span>{{ userInfo.phone }}</span>
          </li>
          <li>
            <label>邮箱：</label>
            <span>{{ userInfo.email }}</span>
          </li>
        </ul>
      </el-card>
    </div>
  </div>

</template>

<script>

export default {
  name: 'UserCenter',
  data() {
    return {
      // 对应的编号
      userId: this.$route.params.userId,
      userType: this.$route.params.type,
      // 静态测试数据
      userInfo: {
        username: '陈嘉力',
        roles: 'woc',
        phone: '13528909',
        email: 'scut@qq.com'
      }
    }
  },
  // 获取userInfo数据（前后端对接）
  created () {
    const userType = JSON.parse(window.sessionStorage.getItem('user')).userType
    if (userType === '1') {
      this.userInfo.roles = '学生'
    } else if (userType === '2') {
      this.userInfo.roles = '教师'
    } else {
      this.userInfo.roles = '管理员'
    }
  }
  // 其他从数据库获取数据。。。

}
</script>

<style lang="less">
.background {
  background-image: url("../assets/img/userCenterbackground.png");
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  .user-center-wrapper {
    opacity: 0.95;
    .user-avatar {
      float: left;
      width: 150px;
      height: 150px;
    }
    .user-info {
      float: left;
      width: 800px;
      margin-left: 50px;
      margin-bottom: 50px;
      li {
        height: 34px;
        line-height: 34px;

        label,
        span {
          display: inline-block;
          vertical-align: middle;
        }

        label {
          width: 80px;
          margin-right: 12px;
          text-align: right;
        }
      }
    }
  }
}
</style>
