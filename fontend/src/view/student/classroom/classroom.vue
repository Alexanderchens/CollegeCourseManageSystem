<template>
<div>
  <el-upload
    class="upload-demo"
    ref="upload"
    action="doUpload"
    :limit="1"
    :file-list="fileList"
    :before-upload="beforeUpload">
    <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
    <a href="./static/moban.xlsx" rel="external nofollow" download="模板"><el-button size="small" type="success">下载模板</el-button></a>
    <!-- <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button> -->
    <div slot="tip" class="el-upload__tip">只能上传excel文件，且不超过5MB</div>
    <div slot="tip" class="el-upload-list__item-name">{{fileName}}</div>
  </el-upload>
  <span slot="footer" class="dialog-footer">
<el-button @click="visible = false">取消</el-button>
<el-button type="primary" @click="submitUpload()">确定</el-button>
</span>
</div>
</template>

<script>
export default {
  name: 'classroom',
  methods: {
    /**
     * @description 上传校验
     * @param file 上传的文件
     * @returns {boolean} 是否上传成功
     */
    beforeUpload (file) {
      console.log(file, '文件')
      this.files = file
      const extension = file.name.split('.')[1] === 'xls'
      const extension2 = file.name.split('.')[1] === 'xlsx'
      const isLt2M = file.size / 1024 / 1024 < 5
      if (!extension && !extension2) {
        this.$message.warning('上传模板只能是 xls、xlsx格式!')
        return
      }
      if (!isLt2M) {
        this.$message.warning('上传模板大小不能超过 5MB!')
        return
      }
      this.fileName = file.name
      return false // 返回false不会自动上传
    },
    /**
     * @description 手动上传
     * @returns {boolean}
     */
    submitUpload () {
      console.log('上传' + this.files.name)
      if (this.fileName === '') {
        this.$message.warning('请选择要上传的文件！')
        return false
      }
      const fileFormData = new FormData()
      fileFormData.append('file', this.files, this.fileName) // filename是键，file是值，就是要传的文件，test.zip是要传的文件名
      const requestConfig = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      this.$http.post('/basedata/oesmembers/upload?companyId=' + this.company, fileFormData, requestConfig).then((res) => {
        if (res && res.code === 0) {
          this.$message({
            message: '操作成功',
            type: 'success',
            duration: 1500,
            onClose: () => {
              this.visible = false
              this.$emit('refreshDataList')
            }
          })
        } else {
          this.$message.error(res.msg)
        }
      })
    }

  }
}
</script>

<style scoped>

</style>
