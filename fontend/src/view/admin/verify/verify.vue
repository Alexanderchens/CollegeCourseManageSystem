<template>
  <div>
    <el-col :span="24">
      <verifyTable id="verifyTable"></verifyTable>
    </el-col>
  </div>
</template>

<script>
import verifyTable from './verifyTable'
export default {
  name: 'verify',
  components: {
    verifyTable
  }
}
</script>

<style lang="less" scoped>

</style>
