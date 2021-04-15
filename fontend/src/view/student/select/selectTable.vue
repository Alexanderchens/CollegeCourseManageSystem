<template>
  <div>
    <p class="title"><i class="el-icon-tickets"></i>学生选课</p>
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
        label="操作"
        prop="choose">
        <template slot-scope="scope">
          <el-button
            id="editBtn"
            @click="handleEdit(scope.$index, scope.row)"
            :type="showBtnType(scope.$index, scope.row)"
            v-text="showBtnText(scope.$index, scope.row)"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'selectTable',
  editBtn: '#editBtn',
  data () {
    return {
      tableData: [{
        name: '计算机网络',
        number: '15/40',
        place: 'A1 404',
        teacher: '黄敏',
        year: '2021',
        semester: '上',
        time: '上课时间1',
        choose: false
      }, {
        name: '量子力学',
        number: '38/40',
        place: 'A3 403',
        teacher: '杨振宁',
        year: '2020',
        semester: '下',
        time: '上课时间2',
        choose: false
      }, {
        name: '软件分析与建模',
        number: '19/40',
        place: 'A1 302',
        teacher: '程兴国',
        year: '2020',
        semester: '上',
        time: '上课时间3',
        choose: false
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
      row.choose = !row.choose
      this.$message({
        showClose: true,
        message: index,
        row,
        type: 'success'
      })
    },
    showBtnType (index, row) {
      return row.choose ? 'danger' : 'primary'
    },
    showBtnText (index, row) {
      return row.choose ? '退选' : '选择'
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

<style scoped>

</style>
