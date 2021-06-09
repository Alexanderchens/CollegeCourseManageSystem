<!--课程信息详情页面-->
<template>
  <div class="container">
    <el-form disabled :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="课程名称" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="授课教师" prop="teacher">
        <el-input v-model="ruleForm.teacher"></el-input>
      </el-form-item>
      <el-form-item label="课程名称" prop="place">
        <el-select v-model="ruleForm.place" placeholder="教室选择">
          <el-option label="区域一" value="shanghai" ></el-option>
          <el-option label="区域二" value="beijing"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="上课时间" required>
        <el-col :span="11">
          <el-form-item prop="date1">
            <el-date-picker :disabled="autoTime" type="date" placeholder="选择日期" v-model="ruleForm.date1" style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="date2">
            <el-time-picker :disabled="autoTime" placeholder="选择时间" v-model="ruleForm.date2" style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="自动排课" prop="autoSchedule">
        <el-switch v-model="ruleForm.autoSchedule" focus="myFocus"></el-switch>
      </el-form-item>
      <el-form-item label="备注" prop="desc">
        <el-input type="textarea" v-model="ruleForm.desc"></el-input>
      </el-form-item>
    </el-form>
    <el-button class="returnBtn" plain @click="returnPage">返回</el-button>
  </div>
</template>

<script>
export default {
  name: 'detailInfo',
  data () {
    return {
      classId: '',
      autoTime: false,
      ruleForm: {
        name: '',
        teacher: '',
        place: '',
        date1: '',
        date2: '',
        autoSchedule: false,
        desc: '',
        application: {}
      },
      rules: {
        name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        place: [
          { required: true, message: '请选择活动区域', trigger: 'change' }
        ],
        date1: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
        ],
        date2: [
          { type: 'date', required: true, message: '请选择时间', trigger: 'change' }
        ],
        desc: [
          { required: true, message: '请填写备注', trigger: 'blur' }
        ]
      }
    }
  },
  /**
   * 页面初始化
   */
  created: function() {
    this.classId = this.$route.query.id
    // 数据库根据id获取数据显示
  },
  methods: {
    myFocus () {
      if (this.ruleForm.autoSchedule === true) {
        this.autoTime = true
      } else {
        this.autoTime = false
      }
    },
    // 返回上一个页面
    returnPage () {
      this.$router.go(-1)
    }
  }
}
</script>

<style lang="less" scoped>
.container {
  padding-top: 100px;
  width: 80%;
}
.returnBtn {
  position: absolute;
  top: 50%;
  left: 50%;
  width:500px;
}
</style>
