<template>
    <div>
      <el-row>
        <el-col :span="24">
          <selectTable id="selectable"></selectTable>
        </el-col>
      </el-row>
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

</style>
