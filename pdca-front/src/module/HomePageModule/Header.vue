<!--home-->
<template>
  <div class="homeContainer">
    <div class="header-content">
      <!-- logo -->
      <div class="logo-container" @click="goHomePage">
        <img
            src="../../assets/logo.png"
            class="logo-image"
        />
      </div>

      <!-- 右侧 -->
      <div class="right-container">
        <button class="unstyle" @click="goHomePage">首页</button>
        <button class="unstyle" @click="goControlConsole">控制台</button>

        <div class="user-info">
          <div v-if="user_data" class="user-details">
            <button class="unstyle">
              <el-avatar
                  size="small"
                  src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
                  class="avatar-image"
              ></el-avatar>
              <span class="user-nickname">{{ user_data.nickname }}</span>
            </button>
            <span class="logout-text">
              <button class="unstyle" @click="loginOut">退出登陆</button>
            </span>
          </div>
          <div v-else>
            <button class="unstyle" @click="toLogin">请登录</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getCookie, GetStorage, removeCookie, RemoveStorage} from "../../utils/token";

export default {
  name: "Header",
  data() {
    return {
      user_data: {},
    };
  },
  created() {
    this.user_data = GetStorage('user_data');
  },
  methods: {
    goHomePage() {
      window.location.href = '/';
    },
    goControlConsole(){
      if (!getCookie('user_token')) {
        this.$router.push({ path: '/login' });
      }
      this.$router.push({ path: '/ControlConsole' });
    },
    toLogin() {
      this.$router.push({ path: '/login' });
    },
    loginOut(){
      removeCookie('user_token')
      RemoveStorage('user_data')
      this.goHomePage()
    },
  },
};
</script>

<style lang="scss" scoped>
.homeContainer {
  width: 1400px;
}

.header-content {
  display: flex;
  height: 60px;
  align-items: center;
  padding: 0 20px;
  box-sizing: border-box;
}

.logo-container {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.logo-image {
  width: 80px;
  height: 80px;
  margin-right: 10px;
}

.right-container {
  display: flex;
  align-items: center;
  margin-left: auto;
}

.unstyle {
  all: unset;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin: 0 10px;
}

.unstyle:hover {
  color: blue; /* Optional: hover effect */
}

.user-info {
  display: flex;
  align-items: center;
}

.user-details {
  display: flex;
  align-items: center;
}

.avatar-image {
  margin-right: 5px;
}



</style>
