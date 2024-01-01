<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name:"APP",
  watch:{
    immediate:true,
    $route:{
      handler(){
        let href =  window.location.href.split('/')
        if(href[3].length !== 1){
          this.$router.push('/404')
        }
      }
    }
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body,html,#app{
  width: 100%;
  height: 100%;
}
#app{
  min-width: 1260px;
}
</style>
