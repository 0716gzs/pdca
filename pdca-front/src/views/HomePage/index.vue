<template>
<div>
<!--  http://www.kaizenjit.com/html/2022/Quality_0614/6312.html-->
  <el-container>
    <el-header>
      <HeaderMenu/>
    </el-header>
    <el-main>
      <BodyMain/>
    </el-main>
    <div v-footer></div>
  </el-container>
</div>
</template>

<script>
import HeaderMenu  from '../../module/HomePageModule/Header.vue'
import BodyMain  from '../../module/HomePageModule/Main.vue'

export default {
  name: "index",

  components: {
    HeaderMenu,
    BodyMain,
  },

  created() {
    this.get_user_info()
  },
  methods: {
    async get_user_info(){
      const res = await this.$api.user.getUserInfo()
      console.log(res)
    }
  }
}
</script>

<style scoped>
.el-header{
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