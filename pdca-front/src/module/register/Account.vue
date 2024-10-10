<template>
  <div>
      <el-form :model="form" class="login-form" ref="form">

        <div>
          <el-form-item prop="nickname" :rules="rules.nickname">
            <el-input
                v-model="form.nickname"
                class="phone-input"
                placeholder="输入名称"
            ></el-input>
          </el-form-item>
        </div>

        <div class="public-div">
          <el-form-item prop="password" :rules="rules.password">
            <el-input
                v-model="form.password"
                class="phone-input"
                placeholder="输入登陆密码"
            ></el-input>
          </el-form-item>
        </div>

        <div class="public-div">
          <el-form-item prop="verify_password" :rules="rules.verify_password">
            <el-input
                v-model="form.verify_password"
                class="verify_password"
                placeholder="在此输入登陆密码"
            ></el-input>
          </el-form-item>
        </div>


        <div class="public-div">
          <el-form-item prop="phone" :rules="rules.phone">
            <el-input
                v-model="form.phone"
                class="phone-input"
                placeholder="请输入手机号"
            ></el-input>
          </el-form-item>
        </div>

        <div class="public-div">
          <el-form-item prop="code" :rules="rules.code">
            <el-row gutter={12} class="code-row">
              <el-col :span="14">
                <el-input
                    v-model="form.code"
                    class="code-input"
                    placeholder="输入验证码"
                ></el-input>
              </el-col>
              <el-col :span="10">
                <el-button
                    :disabled="parent_sent_data.isCodeSending"
                    class="send-code-button"
                    @click="open_DialogVisible"
                >
                  {{parent_sent_data.mes}}
                </el-button>
              </el-col>
            </el-row>
          </el-form-item>
        </div>

        <div class="register-form-checkbox">
          <!-- `checked` 为 true 或 false -->
          <span><el-checkbox v-model="form.user_agreed" @click="handleCheckboxChange"></el-checkbox></span>
          <span style="margin-left: 8px">我已阅读并同意 </span>
          <!-- 控制 <div> 的显示 -->
          <div v-show="showWarning" style="margin-left: 22px; color: red;">
            <span>请勾选同意协议</span>
          </div>
        </div>

        <div class="public-div" style="margin-top: 3px">
          <div>
            <el-form-item>
              <button
                  @click="handleRegister"
                  name="loginAction"
                  type="button"
                  class="next-btn next-btn-primary next-btn-large login-btn"
                  style="margin-right: 12px;"
              >
                注册
              </button>
            </el-form-item>
          </div>
        </div>

      </el-form>

        <Captcha
            @son_sent_data="handleUuid"
            :myProp="parent_sent_data"
            @countdown_data="CountdownData"/>

  </div>
</template>

<script>
import {refsForm} from '../../utils/validate_form';
import {WarningMessage, SuccessMessage, FailMessage} from "../../utils/element_plus_method_encapsulation";
import {registerRules} from '../../utils/rules';
import Captcha from '../../module/public/captcha/index.vue'
import {SetStorage, setCookie} from "../../utils/token";


export default {
  data() {
    return {
      form: {
        nickname: "",
        password: "",
        verify_password: "",
        phone: "",
        code: "",
        user_agreed: false, // 复选框的初始状态
      },
      phone_data_form: {
        phone: "",
        img_code: "", //短信验证码
        uuid: "",
      },
      rules: registerRules(this),
      showWarning: false, // 控制提示信息的显示
      parent_sent_data: {'centerDialogVisible': false, 'phone': '', 'isCodeSending': false, mes:'获取验证码', 'get_captcha': undefined},
    };
  },

  components: {
    Captcha,
  },

  methods: {

    //接受子组件的uuid 进行更新
    handleUuid(son_sent_data) {
      this.phone_data_form.uuid = son_sent_data.uuid;  // 更新接收到的 UUID
      this.phone_data_form.img_code = son_sent_data.img_code;  // 更新接收到的 img_code
      this.parent_sent_data.centerDialogVisible = son_sent_data.centerDialogVisible;  // 更新接收到的 img_code
    },

    CountdownData(countdown_data){
      this.parent_sent_data.mes = countdown_data.mes
      this.parent_sent_data.isCodeSending = countdown_data.isCodeSending
    },

    handleCheckboxChange() {
      this.showWarning = false;  // 初始化显示提示信息状态
    },

    open_DialogVisible() {
      if (!this.form.phone) {
        this.$refs.form.validateField('phone')
      }else{
        if (this.parent_sent_data.centerDialogVisible === true){
          this.parent_sent_data.centerDialogVisible = false
        }else{
          this.parent_sent_data.centerDialogVisible = true
        }
        this.parent_sent_data.phone = this.form.phone
        this.parent_sent_data.get_captcha = true  //点击获取验证码 传入子组件为true 子组件返回false
      }
    },


    async handleRegister() {
      if (!this.form.user_agreed) {
        this.showWarning = true;  // 显示提示信息
        return
      }
      // 使用新的验证方法来返回一个 Promise
      const isValid = await refsForm(this);
      if (isValid) {
        // 合并对象
        delete this.phone_data_form.phone;
        const data = {
          ...this.form,
          ...this.phone_data_form,
        };
        const res = await this.$api.register.register(data)
        SetStorage('user_data', JSON.stringify(res))
        setCookie('user_token', res.token)
        setCookie('refresh_token', res.refresh_token)
        SuccessMessage(this, '注册成功');
        this.$router.push({'path': '/HomePage'})
      } else {
        WarningMessage(this, '表单验证失败');
      }
    },


  }
}
</script>

<style>
.public-div {
  margin-top: -5px;
}

.login-form {
  max-width: 400px;
  margin: 0 auto;
}

.phone-input .el-input__inner {
  width: 20vh;
}

.code-input .el-input__inner {
  border-radius: 4px;
  width: 7vh;
}

.code-row {
  display: flex;
  align-items: center;
}

.send-code-button {
  width: 18vh;
  border-radius: 4px;
  height: 100%;
}

.send-code-button:disabled {
  background-color: #c0c4cc;
  border-color: #dcdfe6;
  cursor: not-allowed;
}

.el-button.primary {
  width: 100%;
}

.register-form-checkbox {
  margin-top: -10px;
  width: fit-content;
  font-size: 12px;
}


#container .schema-form .next-btn {
  width: 100%;
  font-size: 14px;
}

next-btn-primary, .next-btn-primary.visited, .next-btn-primary:link, .next-btn-primary:visited {
  color: #fff;
}

.next-btn-primary {
  border-style: solid;
  background-color: #ff6a00;
  border-color: transparent;
}

.next-btn-large {
  margin: 0;
  height: 40px;
  padding: 0 20px;
  font-size: 14px;
  line-height: 38px;
  border-width: 1px;
}

.next-btn-primary, .next-btn-primary.visited, .next-btn-primary:link, .next-btn-primary:visited {
  color: #fff;
}

.next-btn-primary {
  border-style: solid;
  background-color: #ff6000;
  border-color: transparent;
}

.next-btn, .next-btn:active, .next-btn:focus {
  outline: 0;
}

.next-btn {
  width: 22em;
}

.next-btn, .next-btn *, .next-btn:after, .next-btn :after, .next-btn:before, .next-btn :before {
  box-sizing: border-box;
}

</style>
