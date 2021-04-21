<template>
  <div>
    <el-col :span="24">
      <administrationTable id="verifyTable"></administrationTable>
    </el-col>
  </div>
</template>

<script>
import administrationTable from './administrationTable'
export default {
  name: 'administration',
  components: {
    administrationTable
  }
}
</script>

<style scoped>

</style>
