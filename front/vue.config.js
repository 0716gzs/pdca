const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // 添加此行代码 关闭文件校验
  lintOnSave:false
})
