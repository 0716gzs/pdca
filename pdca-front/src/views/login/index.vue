<template>
  <div>
    <Star style="margin-top: -100px" :source="PhoneSource"/>
  </div>
  <div>
    <div class="login-content">
      <div class=" hjbBpk">
        <el-row>
          <el-col :span="12">
            <div class="wrapper">
              <div class="qr-method method ">
                <div class="pdca-channel">

                </div>
                <div class="qrlogin-title">
                  扫码登陆
                </div>
                <div class="qrcode-wrap app-text-wrap">
                  <div class="pdca-qrcode-wrapper">
                    <img src="" alt="" class="pdca-qrcode">
                  </div>

                  <div class="methods-text">
                    使用<span class="methods">微信扫一扫登陆</span>
                  </div>
                </div>
              </div>
            </div>

          </el-col>

          <el-col :span="12">
            <div class="wrapper">
              <div class="login-container">
                <div class="tabs">
                  <button
                      :class="{ active: isAccount }"
                      @click="isAccount = true"
                  >
                    账号密码登陆
                  </button>
                  <button
                      :class="{ active: !isAccount }"
                      @click="isAccount = false"
                  >
                    手机号登陆
                  </button>
                </div>

                <div class="form-container">
                  <div v-if="isAccount">
                    <AccountLoginFrom />
                  </div>
                  <div v-else>
                    <PhoneLoginFrom :source="PhoneSource"/>
                  </div>

                  <div>
                    <div>
                      <hr style="width: 31vh">
                    </div>
                    <div style="margin-top: 20px">
                      <div>
                        <span>qq</span>
                        <span>支付宝</span>
                        <span>gitee</span>
                      </div>
                    </div>
                  </div>

                </div>
              </div>

            </div>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="24">
            <div class="protocol">

            </div>
            <div class="jAvWcN">
              登录视为您已同意
            </div>
            <div style="margin-top: 20px"></div>
          </el-col>
        </el-row>

      </div>
    </div>
  </div>
</template>

<script>
import PhoneLoginFrom from '../../module/register/Phone.vue';
import AccountLoginFrom from '../../module/login/Account.vue';
import Star from "../../module/public/Star.vue"


export default {
  components: {
    PhoneLoginFrom,
    AccountLoginFrom,
    Star,
  },

  name: "index",

  data() {
    return {
      isAccount: true, // 默认展示手机号注册表单
      PhoneSource: 'login'
    };
  },

}
</script>

<style scoped>
@import './login.css';

.login-container {
  width: 300px;
  margin: 0 auto;
}

.tabs {
  display: flex;
  border-bottom: 1px solid #ddd;
}

.tabs button {
  flex: 1;
  padding: 10px;
  border: none;
  background: #f5f5f5;
  cursor: pointer;
}

.tabs button.active {
  background: #ffffff;
  border-bottom: 2px solid #007bff;
  font-weight: bold;
}

.form-container {
  padding: 20px;
  border-top: none;
}

</style>