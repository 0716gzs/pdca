<template>
  <div>
    <el-dialog
        title="验证码"
        v-model="centerDialogVisible"
        width="30%"
        height="30%"
        :before-close="handleClose"
        center>
      <el-row>
        <el-col :span="10">
          <div class="grid-content bg-purple-light">
            <el-input v-model="data.img_code" placeholder="请输入内容" style="height: 40px"></el-input>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple">
            <el-image
                style="width: 120px; height: 40px"
                :src="verificationImg"
                @click="GetCaptcha(is_click=true)"
            >
            </el-image>
            <a href="#" @click="GetCaptcha(is_click=true)">获取验证码</a>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple-light">
            <el-button @click="handleClose(done=false)">取 消</el-button>
            <el-button type="primary" @click="SendCodeMethod">确 定</el-button>
          </div>
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';
import { FailMessage } from "../../../utils/element_plus_method_encapsulation";

export default {
  props: {
    myProp: {
      type: Object,
      required: true
    }
  },
  watch: {
    myProp: {
      handler(newVal) {
        console.log(newVal)
        if (newVal.get_captcha){
          this.GetCaptcha()
        }
        console.log(newVal.get_captcha)
        this.centerDialogVisible = newVal.centerDialogVisible;
        this.data.phone = newVal.phone;
        this.data.isCodeSending = newVal.isCodeSending;
        this.data.mes = newVal.mes;
      },
      deep: true
    }
  },

  name: "index",
  data() {
    return {
      verificationImg: '',
      data: {'uuid': '', 'img_code': '', 'phone': ''},
      countdown_data: {isCodeSending: false, mes: ''},
      centerDialogVisible: false,
      // 发送验证码
      time: 120,
      captchaNeeded: true, // 倒计时结束后，允许重新获取验证码
    }
  },

  methods: {
    _init(){
      this.captchaNeeded = true; // 倒计时结束后，允许重新获取验证码
      this.data.img_code = ''
    },
    Countdown () {
      let m = setInterval(() => {
        //时间递减
        this.time--
        //按钮不可用
        this.countdown_data.isCodeSending = true
        //内容变换
        this.countdown_data.mes = this.time + '后重新获取验证码'
        this.$emit('countdown_data', this.countdown_data);
        //时间结束后需要变成可以获取验证码的状态  所有参数回复原装
        if (this.time === 0) {
          clearInterval(m)
          this.time = 10
          this.countdown_data.isCodeSending = false
          this.countdown_data.mes = '获取验证码'
          this.$emit('countdown_data', this.countdown_data);
          this._init()
        }

      }, 1000)
    },

    handleClose(done) {
      // Use done() to actually close the dialog
      if (done !== false) {
        done();
      }
      this.data.centerDialogVisible = false;
       // Ensure the dialog state remains as expected
      this.$emit('son_sent_data', this.data);
      this._init()
    },

    async GetCaptcha(is_click=false) {
      if (is_click){
        this._init()
      }
      if (this.captchaNeeded){
        this.data.uuid = uuidv4();
        const res = await this.$api.captcha.captcha(this.data);
        console.log(res)
        this.verificationImg = URL.createObjectURL(res);  // 创建 Blob URL
        this.captchaNeeded = false
      }
    },
    async SendCodeMethod() {
      try {
        const res = await this.$api.pbr.SendCode(this.data);
        console.log(res);
        this.data.centerDialogVisible = false
        this.$emit('son_sent_data', this.data);
        this.Countdown()
      } catch (error) {
        FailMessage(error);
      }
    },
  },
}
</script>

<style scoped>
/* Add any necessary styles here */
</style>
