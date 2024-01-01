<template>
  <div class="pagination">
    <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="total"
        layout="prev, pager, next"
        @current-change="handleCurrentChange"
    >
    </el-pagination>

<!--    <el-pagination-->
<!--        :current-page="currentPage"-->
<!--        :page-size="pageSize"-->
<!--        :total="total"-->
<!--        layout="total, sizes, prev, pager, next, jumper"-->
<!--        :page-sizes="[15, 30, 50, 100]"-->
<!--        @current-change="handleCurrentChange"-->
<!--    >-->
<!--    </el-pagination>-->
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    currentPage: {
      type: Number,
      default: 1,
    },
    pageSize: {
      type: Number,
      default: 10,
    },
    total: {
      type: Number,
      default: 0,
    },
  },
  methods: {
    handleCurrentChange(val) {
      this.$emit("update:currentPage", val);
    },
  },
};
</script>

<style scoped>
.pagination {
  margin-top: 20px;
  text-align: center;
}
</style>
