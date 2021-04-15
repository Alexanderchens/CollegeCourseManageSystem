<template>
  <div>
    <el-card class="classnote-box-card" shadow="hover" header="上课提醒">
      <div v-for="x in 30" :key="x" class="classnote item">
        <i class="el-icon-bell"></i>{{'上课提醒' + x}}
        <el-divider content-position="right">{{ dateTime }}</el-divider>
      </div>
    </el-card>
    <el-card class="message-box-card" shadow="hover" header="发布消息">
      <div v-for="o in 60" :key="o" class="message item">
        <i class="el-icon-bell"></i>{{'列表内容 ' + o }}
        <el-divider content-position="right">{{ dateTime }}</el-divider>
      </div>
    </el-card>
  </div>

</template>

<script>
export default {
  name: 'Message.vue',
  data () {
    const dt = this.getDate({
    })
    return {
      dateTime: dt
    }
  },
  methods: {
    // 获取时间
    getDate () {
      const date = new Date()
      const year = date.getFullYear()
      let month = date.getMonth()
      let day = date.getDate()
      month = month < 10 ? '0' + month : month // 月小于10，加0
      day = day < 10 ? '0' + day : day // day小于10，加0
      return year + '-' + month + '-' + day
    }
  }
}
</script>

<style lang="less" scoped>
  .message {
    font-size: 20px;
    text-align: center;
  }
  .item {
    padding: 18px 0;
  }
  .classnote{
    font-size: 20px;
    text-align: center;
  }

  .message-box-card {
    width: 480px;
    float: right;
  }

  .el-icon-bell{
    float: left;
  }

  .classnote-box-card{
    float: left;
    width: 500px;
  }
</style>
