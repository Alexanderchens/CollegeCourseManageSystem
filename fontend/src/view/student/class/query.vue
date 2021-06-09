<!--学生查询选课情况-->
<template>
    <div>
      <el-card shadow="always">
        <el-form class="form-list">
          <el-row>
            <el-col :span="24">
              <queryTable id="queryTable"></queryTable>
            </el-col>
          </el-row>
        </el-form>
      </el-card>
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
.form-list {
  width: 100%;
  margin: 0 auto;
}

</style>
