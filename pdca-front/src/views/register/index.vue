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
                  扫码注册
                </div>
                <div class="qrcode-wrap app-text-wrap">
                  <div class="pdca-qrcode-wrapper">
                    <img :src="qrcodeUrl" alt="" class="pdca-qrcode">
                  </div>

                  <div class="methods-text">
                    使用<span class="methods">微信扫一扫注册</span>
                  </div>
                </div>
              </div>
            </div>

          </el-col>

          <el-col :span="12">
            <div class="wrapper">
              <div class="register-container">
                <div class="tabs">
                  <button
                      :class="{ active: isPhoneRegister }"
                      @click="isPhoneRegister = true"
                  >
                    手机号注册
                  </button>
                  <button
                      :class="{ active: !isPhoneRegister }"
                      @click="isPhoneRegister = false"
                  >
                    账号密码注册
                  </button>
                </div>

                <div class="form-container">
                  <div v-if="isPhoneRegister">
                    <PhoneRegisterFrom />
                  </div>
                  <div v-else>
                    <AccountRegisterFrom :source="PhoneSource"/>
                  </div>
                </div>
              </div>
            </div>
          </el-col>
        </el-row>

        <div class="protocol">
          <div class="jAvWcN ">
            <span>注册后自动登录视为您已同意</span>
            <span>123123</span>
            <span>123123</span>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
import PhoneRegisterFrom from '../../module/register/Phone.vue';
import AccountRegisterFrom from '../../module/register/Account.vue';
import QRCode from "qrcode";
import {FailMessage} from "../../utils/element_plus_method_encapsulation";
import * as pbr from "../../api/public_request";
import Star from "../../module/public/Star.vue"

export default {
  components: {
    PhoneRegisterFrom,
    AccountRegisterFrom,
    Star,
  },
  async created() {
    this.get_auth_url()
  },

  name: "index",

  data() {
    return {
      isPhoneRegister: true, // 默认展示手机号注册表单
      qrcodeUrl: '',
      PhoneSource: 'register'
    };

  },

  methods: {
    async get_auth_url() {
      try {
        const params = {
          'secret_key': '123123',
        }
        const res = await this.$api.pbr.GetAuthUrl(params)
        // 生成二维码
        this.qrcodeUrl = await QRCode.toDataURL(res.data.auth_url);
      } catch (error) {
        // FailMessage(error)
        console.log(error)
      }
    }
  }

}
</script>

<style scoped>
@import '../login/login.css';

.register-container {
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