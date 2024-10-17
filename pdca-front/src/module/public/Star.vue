<template>
  <div class="star-container">
    <svg
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="star"
    >
      <path
          d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21.02L12 17.77L6.82 21.02L8 14.14L3 9.27L9.91 8.26L12 2Z"
          fill="currentColor"
      />
    </svg>
    <span class="label">
      <button class="starUnstyle" @click="to_page">
        {{msg}}
      </button>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    source: {
      type: Object,
      required: true
    }
  },
  data(){
    return {
      msg: ''
    }
  },
  created(){
    if (this.source === 'register'){
      this.msg = "登陆"
    }else{
      this.msg = "注册"
    }
  },
  methods:{
    to_page(){
      if (this.source === 'register'){
        this.$router.push({ path: '/login' });
      }else if (this.source === 'login'){
        this.$router.push({ path: '/register' });
      }
    },
  }
}
</script>

<style scoped>
.star-container {
  position: relative;
  width: 100px; /* 可以根据需要调整容器的大小 */
  height: 100px;
}

.star {
  position: absolute;
  top: 90px; /* 调整五角星的位置 */
  left: 1058px; /* 调整五角星的位置 */
  width: 90px;
  height: 90px;
  color: #f39c12; /* 设置五角星的颜色 */
  z-index: 1000; /* 确保显示在其他元素之上 */
}

.label {
  position: absolute;
  top: 138px; /* 居中 */
  left: 1104px; /* 居中 */
  transform: translate(-50%, -50%); /* 居中对齐 */
  color: white; /* 文字颜色，可以根据需要调整 */
  font-size: 14px; /* 文字大小，可以根据需要调整 */
  font-weight: bold; /* 文字粗细，可以根据需要调整 */
  z-index: 1001; /* 确保文字在五角星上方 */
}

.starUnstyle {
  all: unset;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin: 0 10px;
}
</style>
