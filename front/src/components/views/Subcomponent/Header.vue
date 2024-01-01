<template>
  <div class="title">
    <div class="title-left">
      <div class="title-left-image"></div>
      <router-link to="/">
        <span class="">博客</span>
      </router-link>
      <router-link to="/usedOrder">
        <span class="">推荐</span>
      </router-link>
      <router-link to="/usedOrder">
        <span class="">学习</span>
      </router-link>
      <router-link to="/advices">
        <span class="">社区</span>
      </router-link>
      <router-link to="/evaluate">
        <span class="">社区</span>
      </router-link>
    </div>
    <div>
    </div>
    <div class="serch">
      <div contenteditable class="inputType" placeholder='请输入文字'></div>
      <div class="button">搜索</div>
    </div>

    <div v-if="user_token">
      <div class="title-right">
        <div class="title-right-image" @mouseenter="avatar" @mouseleave="avatarHide">
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
          <div v-show="hide" class="hide">
            <font class="h_options" @click="header_font('user_info')">用户中心</font>
            <br>
            <font class="h_options" @click="header_font('/aaaa')">aaaa</font>
            <br>
            <font class="h_options" @click="header_font('/bbbb')">bbbb</font>
            <br>
            <font class="h_options" @click="header_font('/cccc')">cccc</font>
            <br>
            <font class="h_options" @click="header_font('/dddd')">dddd</font>
            <br>
            <font class="h_options" @click="header_font('/login')">退出登录</font>
          </div>
        </div>

        <router-link to="/unusedOrder">
          <span class="">会员管理</span>
        </router-link>
        <router-link to="/usedOrder">
          <span class="">动态</span>
        </router-link>
        <router-link to="/advices">
          <span class="">足迹</span>
        </router-link>
        <router-link to="/advices">
          <span class="">发布</span>
        </router-link>
      </div>
    </div>

    <div v-else class="login">
      <router-link to="/login">
        <span class="">请登录</span>
      </router-link>
    </div>

  </div>
</template>

<script>
import {getToken} from '@/utils/token'
import {removeToken} from '@/utils/token'

export default {
  name: 'Header',
  data() {
    return {
      user_token: '',
      hide: false
    }
  },
  methods:{
    avatar() {
      this.hide = true
    },
    avatarHide(){
      this.hide = false
    },

    header_font(font_data){
      if (font_data == '/login') {
        removeToken()
        this.$router.push(font_data)
      }else {
        this.$router.push(font_data)
      }


    }
  },

  mounted() {
    this.user_token = getToken()
    console.log(this.user_token)
  }
}
</script>
<style>
.title {
  margin-left: 0px;
  height: 48px;
  width: 100%;
  background-color: #fff;
  /*border-bottom: 1px solid #DCDCDC;*/
  display: flex;
  justify-content: space-between;
}

.title-left {
  width: 580px;
  height: 48px;
  margin-left: 0;
  background: #fff;
  display: flex;

}

.title-left-image {
  height: 48px;
  width: 120px
}

span {
  font-size: 16px
}

a {
  width: 70px;
  height: 48px;
  color: black;
  margin: 0px 10px;
  text-decoration: none;
  line-height: 48px;
  text-align: center
}

a:hover {
  background-color: #BEBEBE;
}

.serch {
  height: 32px;
  width: 450px;
  background-color: #fff;
  margin: auto;
  display: flex;
}

.inputType {
  width: 400px;
  height: 30px;
  text-indent: 1em;
  line-height: 34px;
  background-color: #fff;
  border: 1px solid black;
  border-top-left-radius: 17px;
  border-bottom-left-radius: 17px;
  font-size: 12px;
}

.inputType:focus {
  outline: none;
  border: 1px solid rgb(230, 32, 213);
}

.button {
  color: #fff;
  text-align: center;
  background: rgba(204, 51, 0, 1);
  border-left: 1px solid rgba(0, 0, 0, 0.45);
  width: 100px;
  height: 32px;
  line-height: 34px;
  border-top-right-radius: 18px;
  border-bottom-right-radius: 18px
}

.title-right {
  width: 420px;
  height: 48px;
  display: flex;
}

.title-right-image {
  width: 50px;
  height: 40px;
  margin: auto;
  margin-left: 10px;
}

.login {
  width: 100px;
  height: 40px;
  margin: auto;
  margin-right: 50px;
}

.hide {
  width: 15em;
  height: 20em;
  /*background-color: antiquewhite;*/
}

.h_options{
  font-size: 17px;
}

</style>



