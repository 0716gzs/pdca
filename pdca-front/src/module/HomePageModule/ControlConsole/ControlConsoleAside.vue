<template>
  <div>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 10px; margin-top: 10px">
      <el-radio-button :value="false">展开</el-radio-button>
      <el-radio-button :value="true">收起</el-radio-button>
    </el-radio-group>

    <el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        @select="handleSelect"
    >
      <el-menu-item-group>
        <el-menu-item index="1">
          <div class="asideMenuText">
            Plan
          </div>
        </el-menu-item>
      </el-menu-item-group>

      <el-menu-item-group>
        <el-menu-item index="2">
          <div class="asideMenuText">
            Do
          </div>
        </el-menu-item>
      </el-menu-item-group>

      <el-menu-item-group>
        <el-menu-item index="3">
          <div class="asideMenuText">
            Check
          </div>
        </el-menu-item>
      </el-menu-item-group>

      <el-menu-item-group>
        <el-menu-item index="4">
          <div class="asideMenuText">
            Action
          </div>
        </el-menu-item>
      </el-menu-item-group>
    </el-menu>
  </div>
</template>

<script>
export default {
  props: {
    activeIndex: {
      type: String,
      default: '2'
    }
  },
  data() {
    return {
      isCollapse: false,
    }
  },
  methods: {
    handleSelect(index) {
      this.$emit('update-active', index);
    },
  },
}
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 100vh;
}

.asideMenuText{
  font-size: 17px;
  font-family: Trattatello;
  width: 150px;
}
</style>
