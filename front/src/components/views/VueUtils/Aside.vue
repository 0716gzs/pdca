<template>
  <div style="height: 100%;">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
             :collapse="isCollapse" router :unique-opened="true" :collapse-transition="true">

      <!--单级菜单-->
      <el-menu-item :index="item.name" v-if="!item.children" v-for="item in resource_list" :key="item.name">
        <i :class="'el-icon-' + item.icon"></i>
        <span slot="title">{{ item.description }}</span>
      </el-menu-item>

      <!--多级菜单-->
      <el-submenu :index=index.toString() v-if="item.children" v-for="(item,index) in resource_list" :key="index">
        <template slot="title">
          <i :class="'el-icon-' + item.icon"></i>
          <span>{{ item.description }}</span>
        </template>
        <el-menu-item-group>
          <el-menu-item :index="subItem.name" v-for="(subItem,subIndex) in item.children" :key="subIndex">
            {{ subItem.description }}
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>


    </el-menu>
  </div>
</template>

<script>
import {GetStorage} from "@/utils/token";
import {decrypt} from "@/utils/utls";

export default {
  name: "Aside",

  data() {
    return {
      resource_list: [],
      isCollapse: true
    }
  },

  methods: {

    resource() {
      const res = JSON.parse(decrypt(GetStorage('UserDate')))
      this.resource_list = res['resources_list']



    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }


  },

  mounted() {
    this.resource()
  }
}
</script>

<style scoped>
.el-menu-vertical-demo {
  height: 42.5rem;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
}
</style>
