<template>
  <div class="wrapper">
    <!-- 页面头部部分 -->
    <div class="header">
      <div>
        <div class="header-left">
          <h3 class="overlap">
            PDCA管理系统
          </h3>
        </div>
        <div class="header-right">
          <div class="header-user-con">
            <!-- 用户头像 -->
            <div class="user-avator">
              <img src="@/assets/logo.png"/>
            </div>
            <!-- 用户名下拉菜单 -->
            <el-dropdown class="user-name" trigger="click" @command="handleCommand">
              <span class="el-dropdown-link"> {{ username }} <i class="el-icon-caret-bottom"></i></span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="loginout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </div>

      </div>
    </div>

    <!-- 页面左侧二级菜单栏，和主体内容区域部分 -->
    <!--    <el-main>-->
    <!--      <router-view></router-view>-->
    <!--    </el-main>-->

  </div>
</template>

<script>
import {decrypt} from "@/utils/utls";
import {GetStorage, RemoveStorage} from "@/utils/token";

export default {
  data() {
    return {}
  },
  computed: {
    username() {
      if (!GetStorage('UserDate')) {
        return ''
      } else {
        return JSON.parse(decrypt(GetStorage('UserDate')))['username']
      }

    },
  },

  created() {

  },
  methods: {
    handleCommand(command) {  // 用户名下拉菜单选择事件
      if (command == 'loginout') {
        RemoveStorage('UserDate')
        RemoveStorage('UserToken')
        RemoveStorage('ResourceList')
        this.$router.push({
          path: '/login'
        });
      }
    }
  }
}
</script>

<style scoped>
.overlap {
  position: absolute;
  top: 25%;
  color: #fff;
  left: 0;
  right: 0;
  font-family: 'lato', sans-serif;
  font-weight: 300;
  font-size: 25px;
  letter-spacing: 4px;
  padding-left: 30px;
  -webkit-background-clip: text;
}
.wrapper {
  width: 100%;
  height: 100%;
}

.header {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  font-size: 22px;
}

.header .logo {
  float: left;
  margin-left: 60px;
  margin-top: 6px;
  height: 29px;
  width: 160px;
  vertical-align: middle;
}

/* --------------- 用户头像区域的样式 ---------------- */
.header-right {
  float: right;
  padding-right: 50px;
}

.header-left {
  float: left;
  padding-left: 50px;
}

.header-user-con {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 70px;
}

.user-avator {
  margin-left: 20px;
}

.user-avator img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.user-name {
  margin-left: 10px;
}

.el-dropdown-link {
  cursor: pointer;
}

.el-dropdown-menu__item {
  text-align: center;
}

</style>
