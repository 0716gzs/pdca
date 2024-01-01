<template>
  <div style="margin: 250px auto;">
    <el-result icon="success" title="注册成功">
    </el-result>
    <div style="padding-left: 40%">
      <div v-if="account_number">
        <h2>您注册的账号：{{account_number}}</h2>

      </div>
      <div v-else>
        <p>您注册的账号：{{account_number}}</p>
      </div>

      <el-button
          type="primary"
          @click="sing_up"
        style="margin-left: 10%"
      >
        去 登 录
      </el-button>

    </div>

  </div>
</template>

<script>
export default {
  name: "success_response",
  data(){
    return{
      account_number:this.$route.query.account_number,
    }
  },
  methods:{
    sing_up(){
      const loading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      setTimeout(() => {
        loading.close();
        this.$router.push("/login")
      }, 200);

    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>
