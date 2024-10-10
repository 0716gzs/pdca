<template>
  <div class="home-pages">
    <div class="layer1"></div>
    <div class="layer2"></div>
    <div class="layer3"></div>
    <div class="layer4"></div>
    <div class="layer5"></div>
    <div class="title">PDCA首页星空</div>
  </div>
  <div v-footer></div>
</template>

<script>

export default {
  name: "index",
  data() {
    //这里存放数据",
    return {
    };
  },

  methods: {


  },

  components: {},
  mounted() {

  }
}
</script>

<style lang="scss">

.title {
  position: absolute;
  top: 50vh;
  color: #fff;
  left: 0;
  right: 0;
  text-align: center;
  font-family: 'lato', sans-serif;
  font-weight: 300;
  font-size: 50px;
  letter-spacing: 10px;
  margin-top: -60px;
  padding-left: 10px;
  -webkit-background-clip: text;
}

.home-pages {
  height: 100vh;
  background: radial-gradient(ellipse at bottom, #1b2735 0vh, #090a0f 100vh);
  overflow: hidden;
}

// sass函数
@function getShadows($n){
  // n 生成多少个随机点
  $shadows: '#{random(100)}vw #{random(100)}vh #fff';
  @for $i from 2 through $n {
    $shadows: '#{$shadows}, #{random(100)}vw #{random(100)}vh #fff'
  }
  @return unquote($shadows);
}

//定义基准时间
$duration: 1000s;
// 数量
$count: 1000;
@for $i from 1 through 5{
  $duration: floor($duration / 2);
  $count: floor($count / 2);
  .layer#{$i} {
    position: fixed;
    $size: #{$i}px;
    width: $size;
    height: $size;
    border-radius: 50vh;
    // 偏移量
    box-shadow: getShadows($count);
    animation: moveup $duration linear infinite;
    //子元素
    &::after{
      content: '';
      position: fixed;
      width: inherit;
      height: inherit;
      left: 0;
      top: 100vh;
      border-radius: inherit;
      box-shadow: inherit;
    }

  }
}



// 动画
@keyframes moveup {
  to{
    transform: translateY(-100vh);
  }
}


</style>