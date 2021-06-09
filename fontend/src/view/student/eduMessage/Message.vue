<template>
  <div class="block">
    <el-timeline>
      <!--      时间戳-->
      <el-timeline-item timestamp="2018/4/12" v-for="x in 10" :key="x" placement="top">
        <el-card>
<!--          信息文本-->
          <p>王小虎 提交于 2018/4/12 20:46 {{x}}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>

</template>

<script>
export default {
  name: 'message',
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

</style>
