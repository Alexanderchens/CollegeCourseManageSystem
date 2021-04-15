<template>
  <div>
    <p class="title"><i class="el-icon-tickets"></i>选课情况查询</p>
    <el-table
      border
      :data="tableData"
      style="width: 100%">
      <el-table-column
        type="index">
      </el-table-column>
      <el-table-column
        prop="name"
        label="课程名称">
      </el-table-column>
      <el-table-column
        sortable
        prop="number"
        label="人数">
      </el-table-column>
        <el-table-column
          prop="place"
          label="教室">
      </el-table-column>
        <el-table-column
          prop="teacher"
          label="教师">
        </el-table-column>
        <el-table-column
          prop="year"
          label="年份"
          sortable
          :filters="[{text: '2018', value: '2018'}, {text: '2019', value: '2019'}, {text: '2020', value: '2020'}, {text: '2021', value: '2021'}]"
          :filter-method="filterHandler"
        >
        </el-table-column>
      <el-table-column
        prop="semester"
        label="学期">
      </el-table-column>
        <el-table-column
          prop="time"
          label="上课时间"
          sortable
        >
      </el-table-column>
      <el-table-column
        prop="status"
        label="状态"
        width="150"
        :filters="[{ text: '待筛选', value: '待筛选' }, { text: '未选上', value: '未选上' }, { text: '已选上', value: '已选上'}]"
        :filter-method="filterStatus"
        filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag
            ref="classTag"
            effect="light"
            :type="showStatus(scope.row.tag)"
            disable-transitions="true">{{scope.row.tag}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">详情</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">退选</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>

export default {
  name: 'queryTable',
  data () {
    // number = 当前选择人数/最后收纳人数
    return {
      tableData: [{
        name: '计算机网络',
        number: '15/40',
        place: 'A1 404',
        teacher: '黄敏',
        tag: '待筛选',
        year: '2021',
        semester: '上',
        time: '上课时间1'
      }, {
        name: '量子力学',
        number: '38/40',
        place: 'A3 403',
        teacher: '杨振宁',
        tag: '未选上',
        year: '2020',
        semester: '下',
        time: '上课时间2'
      }, {
        name: '软件分析与建模',
        number: '19/40',
        place: 'A1 302',
        teacher: '程兴国',
        tag: '已选上',
        year: '2020',
        semester: '上',
        time: '上课时间3'
      }]
    }
  },
  methods: {
    show () {
      console.log(this.$refs.classTag.type)
    },
    showStatus (index) {
      if (index === '待筛选') {
        return 'primary'
      } else if (index === '未选上') {
        return 'danger'
      } else return 'success'
    },
    handleEdit (index, row) {
      console.log(index, row)
      this.$message({
        showClose: true,
        message: index,
        row,
        type: 'success'
      })
    },
    handleDelete (index, row) {
      console.log(index, row)
      this.$message({
        showClose: true,
        message: index,
        row,
        type: 'success'
      })
    },
    formatter (row, column) {
      return row.address
    },
    filterStatus (value, row) {
      return row.tag === value
    },
    filterHandler (value, row, column) {
      const property = column.property
      return row[property] === value
    }
  }
}
</script>

<style lang="less" scoped>

</style>
