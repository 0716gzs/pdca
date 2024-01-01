<template>
  <div class="table-component">
    <el-table :data="tableData" border class="custom-table">
      <el-table-column v-for="column in columns" :key="column.prop" :label="column.label" :prop="column.prop">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "TableComponent",
  props: {
    tableData: {
      type: Array,
      default: () => [],
    },
    columns: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style scoped>
.table-component {
  margin-top: 20px;
}

.custom-table {
  width: 100%;
}

.custom-table .el-table__header-wrapper {
  background-color: #f5f7fa;
}

.custom-table .el-table__header th {
  color: #333;
  font-weight: bold;
}

.custom-table .el-table__body td {
  color: #666;
}

.custom-table .el-table__row:nth-child(even) {
  background-color: #f9fafc;
}

.custom-table .el-table__row:hover {
  background-color: #eaf1fc;
}
</style>
