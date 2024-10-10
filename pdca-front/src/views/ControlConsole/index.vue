<template>
  <div class="common-layout">
    <el-container>
      <el-header><HeaderMenu/></el-header>
      <el-container>
        <el-aside width="200px">
          <ControlConsoleAside
              :activeIndex="activeIndex"
              @update-active="updateActiveIndex"
          />
        </el-aside>
        <el-main>
          <ControlConsoleMain :currentIndex="activeIndex"/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import HeaderMenu from '../../module/HomePageModule/Header.vue'
import ControlConsoleAside from '../../module/HomePageModule/ControlConsole/ControlConsoleAside.vue'
import ControlConsoleMain from '../../module/HomePageModule/ControlConsole/ControlConsoleMain.vue'

export default {
  name: "index",
  components: {
    HeaderMenu,
    ControlConsoleAside,
    ControlConsoleMain,
  },
  data() {
    return {
      activeIndex: '2'
    }
  },
  methods: {
    updateActiveIndex(index) {
      this.activeIndex = index;
    }
  }
}
</script>

<style scoped>
.el-header {
  margin-top: -60px;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-main {
  width: 1445px;
  margin-left: -10px;
  color: #333;
  text-align: center;
  line-height: 100%;
}
</style>
