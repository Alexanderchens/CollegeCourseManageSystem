
<template>
  <div>
    <p class="title"><i class="el-icon-tickets"></i>课程待审核信息</p>
    <el-table
      border
      :data="tableData"
      style="width: 100%">
      <el-table-column
        type="index">
      </el-table-column>
      <el-table-column
        sortable
        prop="name"
        label="课程名称">
      </el-table-column>
      <el-table-column
        prop="teacher"
        label="申请老师"
        sortable
        :filters="[{text: '', value: ''}, {text: '', value: ''}, {text: '', value: ''}, {text: '', value: ''}, {text: '', value: ''}]"
        filter-method="filterHandler">
      </el-table-column>
      <el-table-column
        prop="time"
        label="时间"
        sortable
        :filters="[{text: '2018-01-01', value: '2018-01-01'}, {text: '2018-01-02', value: '2018-01-02'}, {text: '2018-01-03', value: '2018-01-03'}, {text: '2018-01-04', value: '2018-01-04'}, {text: '2018-01-05', value: '2018-01-05'}]"
        :filter-method="filterHandler">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">详情</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">驳回</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'verifyTable',
  data () {
    return {
      // 测试数据
      tableData: [{
        name: '计算机网络',
        teacher: '黄敏',
        time: '2021-01-01'
      }, {
        name: '数据结构',
        teacher: '黄敏',
        time: '2021-01-02'
      }, {
        name: '操作系统',
        teacher: '王国华',
        time: '2021-01-03'
      }]
    }
  },
  methods: {
    handleEdit (index, row) {
      console.log(index, row)
      this.selectRouter(index)
      this.$message({
        showClose: true,
        message: '进入审核',
        row,
        type: 'info'
      })
    },
    selectRouter (index) {
      this.$router.push('application/' + index.toString())
    },
    handleDelete (index, row) {
      console.log(index, row)
      this.tableData.splice(this.tableData.index, 1)
      this.$message({
        showClose: true,
        message: '驳回成功',
        row,
        type: 'success'
      })
    },
    formatter (row, column) {
      return row.address
    },
    filterTag (value, row) {
      return row.tag === value
    },
    filterHandler (value, row, column) {
      const property = column.property
      return row[property] === value
    }
  }
}
</script>

<style scoped>

</style>
