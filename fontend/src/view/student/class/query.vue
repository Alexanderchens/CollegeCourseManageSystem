<template>
    <div>
      <el-row>
        <el-col :span="24">
          <queryTable id="queryTable"></queryTable>
        </el-col>
      </el-row>
    </div>
</template>

<script>
import QueryTable from './queryTable'

export default {
  name: 'query',
  components: {
    QueryTable
  }
}
</script>

<style scoped>

</style>
