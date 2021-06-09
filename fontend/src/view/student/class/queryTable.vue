<!--学生查询选课情况表格-->
<template>
  <div>
    <p class="title"><i class="el-icon-tickets"></i>选课情况查询</p>
    <el-table
      border
      :data="tableData"
      style="width: 100%">
<!--      编号-->
      <el-table-column
        prop="classId"
        label="编号"
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
      <el-table-column label="操作" fixed="right">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleDetail(scope.$index, scope.row)">详情</el-button>
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
      // 测试数据
      tableData: [{
        classId: 0,
        name: '计算机网络',
        number: '15/40',
        place: 'A1 404',
        teacher: '黄敏',
        tag: '待筛选',
        year: '2021',
        semester: '上',
        time: '上课时间1'
      }, {
        classId: 1,
        name: '量子力学',
        number: '38/40',
        place: 'A3 403',
        teacher: '杨振宁',
        tag: '未选上',
        year: '2020',
        semester: '下',
        time: '上课时间2'
      }, {
        classId: 2,
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
    /**
     *  @description 不用理会，前端展示函数
     *  @param index
     */
    showStatus (index) {
      if (index === '待筛选') {
        return 'primary'
      } else if (index === '未选上') {
        return 'danger'
      } else return 'success'
    },
    /**
     * 详情页面
     * @param index 顺序
     * @param row 行信息
     */
    handleDetail (index, row) {
      console.log(index, row)
      this.$message({
        showClose: true,
        message: '查看课程详细信息',
        type: 'success'
      })
      this.$router.push({
        path: '/classInfo/',
        query: {
          id: row.classId
        }
      })
    },
    /**
     * 退选
     * @param index
     * @param row
     */
    handleDelete (index, row) {
      console.log(index, row)
      this.tableData.splice(index, 1)
      this.$message({
        showClose: true,
        message: index,
        type: 'success'
      })
    },
    /**
     * 前端展示函数
     * @param row
     * @param column
     * @returns {*}
     */
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
