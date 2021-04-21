<template>
  <div>
    <el-card header="发布通知" style="color: #3d95ff">
      <el-row v-for="value in notes" :key="value">
          <el-link icon="el-icon-edit" style="list-style-position: inside">{{value.title}}</el-link>
          <el-button type="danger" icon="el-icon-delete" circle style="float: right"></el-button>
          <el-divider content-position="right">{{ value.body }}</el-divider>
      </el-row>
    </el-card>
    <el-row>
      <el-card style="margin-top: 100px">
        <quill-editor class="editor"
                      ref="myTextEditor"
                      v-model="content"
                      :options="editorOption"
                      @blur="onEditorBlur($event)"
                      @focus="onEditorFocus($event)"
                      @ready="onEditorReady($event)"
                      @change="onEditorChange($event)"></quill-editor>
        <el-button type="primary" @click.prevent="submit">提交</el-button>
      </el-card>
    </el-row>
  </div>
</template>

<script>
import { quillEditor } from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

export default {
  name: 'notification.vue',
  components: {
    quillEditor
  },
  data () {
    return {
      notes: [],
      note: {
        dateTime: null,
        content: null
      },
      editorOption: {
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'], // 加粗 斜体 下划线 删除线
            ['blockquote', 'code-block'], // 引用  代码块
            [{ header: 1 }, { header: 2 }], // 1、2 级标题
            [{ list: 'ordered' }, { list: 'bullet' }], // 有序、无序列表
            [{ script: 'sub' }, { script: 'super' }], // 上标/下标
            [{ indent: '-1' }, { indent: '+1' }], // 缩进
            // [{'direction': 'rtl'}],                         // 文本方向
            [{ size: ['small', false, 'large', 'huge'] }], // 字体大小
            [{ header: [1, 2, 3, 4, 5, 6, false] }], // 标题
            [{ color: [] }, { background: [] }], // 字体颜色、字体背景颜色
            [{ font: [] }], // 字体种类
            [{ align: [] }], // 对齐方式
            ['clean'], // 清除文本格式
            ['link', 'image', 'video'] // 链接、图片、视频
          ] // 工具菜单栏配置
        },
        placeholder: '请输入教务通知', // 提示
        readyOnly: false, // 是否只读
        theme: 'snow', // 主题 snow/bubble
        syntax: true // 语法检测
      }
    }
  },

  methods: {
    // 失去焦点
    onEditorBlur (editor) {},
    // 获得焦点
    onEditorFocus (editor) {},
    // 开始
    onEditorReady (editor) {},
    // 值发生变化
    onEditorChange (editor) {
      this.note.content = editor.html
      console.log(editor)
    },
    // 显示当前时间（年月日时分秒）
    timeFormate () {
      const year = new Date().getFullYear()
      const month = new Date().getMonth() + 1 < 10 ? '0' + (new Date().getMonth() + 1) : new Date().getMonth() + 1
      const date = new Date().getDate() < 10 ? '0' + new Date().getDate() : new Date().getDate()
      const hh = new Date().getHours() < 10 ? '0' + new Date().getHours() : new Date().getHours()
      const mm = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes()
      // let ss =new Date(timeStamp).getSeconds() < 10? "0" + new Date(timeStamp).getSeconds(): new Date(timeStamp).getSeconds();
      // let week = new Date(timeStamp).getDay();
      // let weeks = ["日","一","二","三","四","五","六"];
      // let getWeek = "星期" + weeks[week];
      this.nowTime = year + '-' + month + '-' + date + '-' + '-' + hh + ':' + mm
    },
    nowTimes () {
      this.timeFormate(new Date())
      setInterval(this.nowTimes, 1000)
      // this.clear()
    },
    // clear(){
    //   clearInterval(this.nowTimes)
    //   this.nowTimes = null;
    // },
    submit () {
      this.note.dateTime = new Date().getFullYear() + '-' + new Date().getMonth() + 1 < 10 ? '0' + (new Date().getMonth() + 1) : new Date().getMonth() + 1 + '-' + new Date().getDate() < 10 ? '0' + new Date().getDate() : new Date().getDate()
      this.notes.unshift(this.note)
      this.$http.post('http://jsonplaceholder.typicode.com/posts', {
        body: this.content,
        userId: 1
      })
        .then(function (data) {
          console.log(data)
        })
    }
  },
  created () {
    this.$http.get('http://jsonplaceholder.typicode.com/posts')
      .then(function (data) {
        // console.log(data)
        this.notes = data.body.slice(0, 10)
      })
  },
  computed: {
    editor () {
      return this.$refs.myTextEditor.quillEditor
    }
  },
  mounted () {
    // console.log('this is my editor',this.editor);
  }
}
// editorOption里是放图片上传配置参数用的，例如：
// action:  '/api/product/richtext_img_upload.do',  // 必填参数 图片上传地址
// methods: 'post',  // 必填参数 图片上传方式
// token: '',  // 可选参数 如果需要token验证，假设你的token有存放在sessionStorage
// name: 'upload_file',  // 必填参数 文件的参数名
// size: 500,  // 可选参数   图片大小，单位为Kb, 1M = 1024Kb
// accept: 'multipart/form-data, image/png, image/gif, image/jpeg, image/bmp, image/x-icon,image/jpg'  // 可选 可上传的图片格式

</script>

<style lang="less" scoped>

</style>
