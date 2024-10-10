<template>
<div>
<!--  轮播图-->
  <div class="div_distance">
    <el-carousel :interval="4000" type="card" height="350px">
      <el-carousel-item v-for="(image, index) in CarouselMap" :key="index" class="carousel-item">
        <img  :src="image" :alt="'Image ' + index" class="CarouselMapImage"/>
      </el-carousel-item>
    </el-carousel>
  </div>

  <div class="div_distance plan">
    <el-row>
      <el-col :span="12">
        <div class="grid-content bg-purple">
          <div>
            <img src="" alt="">
          </div>
      </div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>

  <div class="div_distance Do">
    <el-row>
      <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>

  <div class="div_distance Check">
    <el-row>
      <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>

  <div class="div_distance Act">
    <el-row>
      <el-col :span="12"><div class="grid-content bg-purple"></div></el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>


</div>
</template>

<script>
export default {
  name: "Main",
  data () {
    return {
      CarouselMap: []
    }
  },

  created() {
    this.loadImages();
  },

  methods: {
    async loadImages() {
      // 动态导入 carousel_map 目录下的所有图片
      const importImages = import.meta.glob('/src/assets/carousel_map/*.{jpg,jpeg,png,gif,svg}');

      // 使用 Promise.all 处理所有图片的动态导入
      const imageModules = await Promise.all(
          Object.values(importImages).map((importFn) => importFn())
      );

      // 将加载的图片路径存储到 images 中
      this.CarouselMap = imageModules.map((module) => module.default);

      console.log(this.CarouselMap)
    }
  }


}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

/*轮播图下模块*/

.bg-purple {
  background: #d3dce6;
  height: 50vh;
}
.bg-purple-light {
  background: #e5e9f2;
  height: 50vh;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.CarouselMapImage {
  width: 100%;
  height: 350px;
}

.div_distance{
  margin-top: 30px;
}
</style>