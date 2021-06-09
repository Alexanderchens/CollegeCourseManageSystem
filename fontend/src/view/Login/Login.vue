<!--登录界面-->
<template>
<!--  背景图片（华为mateX2壁纸）-->
    <div class="login_container" :style="'background-image:url('+ Background +')'">
      <div class="login_box">
        <div class="avatar_box">
          <img src="../../assets/img/logo.png" alt="">
        </div>
<!--        登录表单区域-->
        <el-form ref="loginFormRef" :rules="loginFormRules" :model=" loginForm " label-width="0px" class="login_form">
          <div class="form_title">选课管理系统</div>
<!--          用户名-->
          <el-form-item prop="username">
            <el-input  v-model="loginForm.username" placeholder="用户名" prefix-icon="el-icon-user" clearable></el-input>
          </el-form-item>
<!--        密码-->
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" placeholder="密码" show-password prefix-icon="el-icon-lock"></el-input>
        </el-form-item>
<!--          单选-->
          <el-form-item class="type_radio" >
            <el-radio v-model="loginForm.userType" label="1">学生</el-radio>
            <el-radio v-model="loginForm.userType" label="2">教师</el-radio>
            <el-radio v-model="loginForm.userType" label="3">管理员</el-radio>
          </el-form-item>
<!--        按钮-->
        <el-form-item class="btns">
          <el-button type="primary" round @click="login">登录</el-button>
          <el-button type="info" round @click="resetLoginForm">重置</el-button>
        </el-form-item>
        </el-form>
      </div>
    </div>
</template>

<script>
import Background from '../../assets/img/loginBackground.jpg'
export default {
  data () {
    return {
      Background,  // 背景图片url
      // 登录表单
      loginForm: {
        username: '',  // 用户名（可能就是学号那些）
        password: '',  // 密码
        userType: '1'     //  登录类型：1：学生 2：老师 3：管理员
      },
      // 前端简单校验登录
      loginFormRules: {
        username: [
          {
            required: true,
            message: '请输入用户名称',
            trigger: 'blur'
          },
          // 用户名为正整数校验
          {
            pattern: /^[0-9.-]+$/,
            message: '用户名格式错误',
            trigger: 'blur'
          }
        ],
        password: [{ required: true, message: '请输入用户名称', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 点击重置信息按钮
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    /**
     * 登录函数
     */
    login () {
      this.$refs.loginFormRef.validate(async (valid) => {
        console.log(valid)
        // 登录校验用户信息
        if (!valid) {
          this.$message.warning('错误，请重新输入')
          return
        }
        // const { data: res } = await this.$http.post('login', this.loginForm)
        // if (res.meta.status !== 200) return this.$message.error('登录失败')
        console.log('通过验证')
        this.$message.success('登录成功')
        // window.sessionStorage.setItem('token', res.data.token)
        // 跳转对应人员的页面
        if (this.loginForm.userType === '1') {
          window.sessionStorage.setItem('user', JSON.stringify({
            userType: this.loginForm.userType,
            username: this.loginForm.username
          }))
          this.$router.push({
            path: '/student'
          })
        } else if (this.loginForm.userType === '2') {
          window.sessionStorage.setItem('user', JSON.stringify({
            userType: this.loginForm.userType,
            username: this.loginForm.username
          }))
          this.$router.push('/student')
        } else {
          window.sessionStorage.setItem('user', JSON.stringify({
            userType: this.loginForm.userType,
            username: this.loginForm.username
          }))
          this.$router.push('/admin')
        }
      })
    }
  }
}

</script>

<style lang="less" scoped>
// 背景样式
.login_container{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  background-size: cover;
  .form-box {
    width: 320px;
    padding: 15px 30px 20px;
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 15px 30px 0 rgba(0, 0, 1, .1);
    .form-title {
      margin: 0 auto 35px;
      text-align: center;
      color: #707070;
      font-size: 18px;
      letter-spacing: 2px;
    }
  }
}
// 登录表单的样式
.login_box{
    border-radius: 1rem;
    width: 450px;
    height: 350px;
    background-color: #fff;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
  }

  .avatar_box{
    width: 80px;
    height: 80px;
    border: 1px solid #eee;
    border-radius: 50%;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    img{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }

  .btns{
    display: flex;
    justify-content: center;
  }

  .login_form{
    position: absolute;
    top: 30px;
    bottom: 0px;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
  }

  .type_radio{
    display: flex;
    justify-content: center;
  }

  .form_title{
      width: 100%;
      line-height: 50px;
      text-align: center;
      font-size: 20px;
      color: #6868ea;
      border-bottom: 1px solid #dddddd;
      font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
</style>
