<template>
  <div class="filter-container">
    <div v-for="(filter, index) in filters" :key="index" class="filter-item">
      <el-input
          v-model="filter.value"
          :placeholder="filter.placeholder"
          class="filter-input"
      />
      <el-button type="primary" @click="applyFilter(filter.value)">筛选</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DynamicFilter',
  props: {
    initialFilters: {
      type: Array,
      default: () => [{ placeholder: '请输入条件', value: '' }]
    }
  },
  data() {
    return {
      filters: this.initialFilters // 使用父组件传递的初始条件
    };
  },
  methods: {
    applyFilter(value) {
      if (value) {
        // 在这里处理每个条件的筛选逻辑
        this.$emit('filter-applied', value); // 触发事件将条件传递给父组件
      } else {
        this.$message.warning('条件不能为空');
      }
    }
  }
};
</script>

<style scoped>
.filter-container {
  display: flex;
  flex-direction: column; /* 垂直排列筛选项 */
  gap: 10px; /* 筛选项之间的间距 */
}

.filter-item {
  display: flex; /* 水平排列输入框和按钮 */
  align-items: center; /* 垂直居中对齐 */
}

.filter-input {
  width: 200px; /* 设置输入框宽度 */
  margin-right: 10px; /* 输入框和按钮之间的间距 */
}
</style>
