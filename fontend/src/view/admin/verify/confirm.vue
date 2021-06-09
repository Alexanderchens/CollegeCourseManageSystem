<!--审核页面-->
<template>
    <div style="padding-top: 100px;">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="课程名称" prop="name">
          <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="授课教师" prop="teacher">
          <el-input v-model="ruleForm.teacher"></el-input>
        </el-form-item>
        <el-form-item label="课程名称" prop="place">
          <el-select v-model="ruleForm.place" placeholder="教室选择">
            <el-option label="区域一" value="shanghai"></el-option>
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
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">完成审核</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
</template>

<script>
export default {
  name: 'confirm',
  data () {
    return {
      id: this.$route.params.id,
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
  created () {
    this.$http.get('http://jsonplaceholder.typicode.com/posts/' + this.id.toString())
      .then(function (data) {
        console.log(data)
      })
  },
  methods: {
    myFocus () {
      if (this.ruleForm.autoSchedule === true) {
        this.autoTime = true
      } else {
        this.autoTime = false
      }
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="less" scoped>

</style>
