<template>
    <div>
      <el-card shadow="always">
        <el-form class="form-list">
          <el-row>
            <el-col :span="24">
              <selectTable id="selectable"></selectTable>
            </el-col>
          </el-row>
        </el-form>
      </el-card>
    </div>
</template>

<script>
import SelectTable from './selectTable'

export default {
  name: 'select',
  components: {
    SelectTable
  }
}
</script>

<style scoped>
.form-list {
  width: 100%;
  margin: 0 auto;
}
</style>
