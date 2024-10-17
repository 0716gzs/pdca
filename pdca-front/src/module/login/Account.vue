<template>
  <el-form :model="form" class="login-form" ref="form">

    <div style="margin-top: 2vh">
      <el-form-item prop="account_email" :rules="rules.account_email">
        <el-input
            v-model="form.account_email"
            class="phone-input"
            placeholder="输入邮箱/10位ID"
        ></el-input>
      </el-form-item>
    </div>

    <div class="login-account-public-div">
      <el-form-item prop="password" :rules="rules.password">
        <el-input
            v-model="form.password"
            class="phone-input"
            placeholder="输入登陆密码"
        ></el-input>
      </el-form-item>
    </div>

    <div class="form-checkbox">
      <!-- `checked` 为 true 或 false -->
      <span><el-checkbox v-model="form.login_user_agreed" @click="handleLoginCheckboxChange"></el-checkbox></span>
      <span style="margin-left: 8px">我已阅读并同意 </span>
      <!-- 控制 <div> 的显示 -->
      <div v-show="loginShowWarning" style="margin-left: 22px; color: red;">
        <span>请勾选同意协议</span>
      </div>
    </div>


    <div class="login-account-public-div" style="margin-top: 3px">
      <div class="login-account-public-div">
        <el-form-item>
          <button
              @click="handleAccountLogin"
              name="loginAction"
              type="button"
              class="next-btn next-btn-primary next-btn-large login-btn"
              style="margin-right: 12px;"
          >
            登陆
          </button>
        </el-form-item>
      </div>


    </div>

  </el-form>
</template>

<script>
import {LoginAccountRules} from '../../utils/rules'
import {refsForm} from "../../utils/validate_form";
import {FailMessage, SuccessMessage, WarningMessage} from "../../utils/element_plus_method_encapsulation";
import {SetStorage, setCookie} from "../../utils/token";
export default {
  data() {
    return {
      form: {
        login_user_agreed: false
      },
      rules: LoginAccountRules(),
      loginShowWarning: false, // 控制提示信息的显示
    };
  },
  methods: {
    handleLoginCheckboxChange() {
      this.loginShowWarning = false;  // 初始化显示提示信息状态
    },
    async handleAccountLogin() {
      // 验证是否勾选我已同意
      if(!this.form.login_user_agreed){
        this.loginShowWarning = true;  // 显示提示信息
        return
      }

      // 使用新的验证方法来返回一个 Promise
      const isValid = await refsForm(this);
      if (isValid) {
        // 合并对象
        const res = await this.$api.login.login(this.form)
        SetStorage('user_data', JSON.stringify(res))
        console.log(123123)
        console.log(res)
        setCookie('user_token', res.token)
        setCookie('refresh_token', res.refresh_token)
        SuccessMessage(this, '登陆成功');
        this.$router.push({'path': '/HomePage'})
      } else {
        WarningMessage(this, '表单验证失败');
      }

    }
  },
}
</script>

<style>
.login-account-public-div{
  margin-top: 4vh;
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
  width: 19vh;
}

.code-row {
  display: flex;
  align-items: center;
}

.send-code-button {
  width: 14vh;
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

.form-checkbox {
  padding-top: 2vh;
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
