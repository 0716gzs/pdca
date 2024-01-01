<template>
  <div class="container">

    <el-container>
      <el-header>
        <Header></Header>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <Aside></Aside>
        </el-aside>
        <el-container>
          <el-main>
            <router-view></router-view>
          </el-main>
          <el-footer>Footer</el-footer>
        </el-container>
      </el-container>
    </el-container>


  </div>
</template>

<script>
import Aside from "@/components/views/VueUtils/Aside.vue";
import Header from "@/components/views/VueUtils/Header.vue";

export default {
  name: 'index',
  data() {
    //这里存放数据",
    return {
    };
  },

  methods: {


  },

  components: { Aside, Header},
  mounted() {

  }
}

</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
}

.el-header, .el-footer {
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  color: #333;
  text-align: center;
}

.el-main {
  color: #333;
  text-align: center;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

</style>
