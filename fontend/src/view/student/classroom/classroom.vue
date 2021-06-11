<template>
  <div class="table-classic-wrapper">
    <Hints>
      <template slot="hintName">空教室查询</template>
      <template slot="hintInfo">
      </template>
    </Hints>
    <el-card shadow="always">
      <!-- 查询栏 -->
      <el-form
        ref="searchForm"
        :inline="true"
        :model="listQuery"
        label-width="90px"
        class="search-form"
      >
        <el-form-item label="周数">
          <el-select v-model="listQuery.weekNum" placeholder="选择你的周数">
            <el-option :value="x" :label="`第${(x)}周`" v-for="x in 20" v-bind:key="x"/>
          </el-select>
        </el-form-item>
<!--        星期几-->
        <el-form-item label="星期">
          <el-select v-model="listQuery.dayOfWeek" placeholder="星期">
            <el-option :value="0" label="星期天" />
            <el-option :value="1" label="星期一" />
            <el-option :value="2" label="星期二" />
            <el-option :value="3" label="星期三" />
            <el-option :value="4" label="星期四" />
            <el-option :value="5" label="星期五" />
            <el-option :value="6" label="星期六" />
          </el-select>
        </el-form-item>
<!--        时段多选-->
        <el-form-item label="时段">
          <el-select  v-model="listQuery.timeIntervals" placeholder="请选择时段" multiple>
            <el-option label="选择所有" value="all"></el-option>
            <el-option v-for="item in classes" :label="item.label" :value="item.value" :key="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">查询</el-button>
        </el-form-item>
      </el-form>
      <!-- 表格栏 -->
      <el-table
        ref="multipleTable"
        v-loading="listLoading"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 100%"
        size="medium">
        <el-table-column
          prop="building"
          label="楼栋"
          width="180">
        </el-table-column>
        <el-table-column
          prop="classroom"
          label="教室"
          width="auto">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>

import Hints from '../../../components/Hints'

export default {
  name: 'Table',
  components: { Hints },
  data() {
    return {
      // 数据列表加载动画
      listLoading: true,
      // 查询列表参数对象
      listQuery: {
        weekNum: undefined,  // 第几周
        dayOfWeek: undefined,  // 星期几
        timeIntervals: undefined  // 时段  第一二节，三四节......
      },
      // 时段选项信息
      classes: [
        { value: '1', label: '一~二节' },
        { value: '2', label: '三~四节' },
        { value: '3', label: '五~六节' },
        { value: '4', label: '七~八节' },
        { value: '5', label: '九~十节' },
        { value: '6', label: '十一~十二节' }
      ],
      tableData: [

      ]
    }
  },
  created() {
    this.fetchData()
  },
  watch: {
    'listQuery.timeIntervals': function(val, oldval) {
      const newindex =  val.indexOf('all')
      const oldindex =  oldval.indexOf('all')   // 获取val和oldval里all的索引,如果没有则返回-1
      if (newindex != -1 && oldindex == -1 && val.length > 1) {
        // 如果新的选择里有勾选了选择所有选择所有 则 只直线勾选所有整个选项
        this.listQuery.timeIntervals = ['all']
      }
      else if (newindex != -1 && oldindex != -1 && val.length > 1) {
        // 如果操作前有勾选了选择所有且当前也选中了勾选所有且勾选数量大于1  则移除掉勾选所有
        this.listQuery.timeIntervals.splice(val.indexOf('all'), 1)
      }
    }
  },
  methods: {
    // 获取空教室列表
    fetchData() {
      this.listLoading = true
      // 获取数据列表接口
      this.getTableList(this.listQuery)
    },
    // 获取数据列表接口
    getTableList: function (query) {
      this.axios({
        url: '',
        data: { query },
        method: 'post'
      }).then((res) => {
        console.log(res)
        // 后面获取数据库数据,并对tableData进行赋值
        this.tableData = res.data
      }).catch((e) => {
        console.log(e)
      }).finally(() => {
        this.listLoading = false
      })
    },
    // 查询数据
    onSubmit() {
      this.fetchData()
    }
  }
}
</script>

<style lang="less">
.table-classic-wrapper {
  .el-card {
    min-height: 656px;
  }
  .control-btns {
    margin-bottom: 20px;
  }
  .search-form {
    padding-top: 18px;
    margin-bottom: 15px;
    background-color: #f7f8fb;
  }
  .el-table thead {
    font-weight: 600;
    th {
      background-color: #f2f3f7;
    }
  }
  .dialog-form {
    .el-input {
      width: 380px;
    }
    .footer-item {
      margin-top: 50px;
      text-align: right;
    }
  }
  .upload-box,
  .export-data {
    width: 300px;
    margin: 0 auto 30px;
  }
  .upload-box {
    width: 156px;
    .files-upload {
      color: #20a0ff;
    }
  }
  .hints {
    font-size: 12px;
    color: #aaa;
    text-align: center;
  }
}
</style>
