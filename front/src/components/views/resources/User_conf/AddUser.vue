<template>
  <div style="margin-left: 180px">
    <table-component :table-data="tableData" :columns="columns"></table-component>
    <Pagination></Pagination>

<!--    <pagination-->
<!--        :current-page="currentPage"-->
<!--        :page-size="pageSize"-->
<!--        :total="total"-->
<!--        @update:currentPage="handlePageChange"-->
<!--    ></pagination>-->
  </div>
</template>

<script>
import Pagination from "@/components/views/VueUtils/pagination"
import TableComponent from "@/components/views/VueUtils/TableComponent";
import UserColumns from "@/utils/const"

export default {
  name: "AddUser",
  components: {
    Pagination,
    TableComponent,
  },
  data() {
    return {
      currentPage: 2,
      pageSize: 1,
      total: 0,

      tableData: [
        // 表格数据
      ],
      columns: UserColumns
    };
  },
  methods: {
    async handlePageChange(val) {
      console.log(val)
      // 更新当前页的数据
      const pagination = {
        'pageNo': this.currentPage,
        'pageSize': this.pageSize,
      }
      try {
        const res = await this.$api.rbac.getUserAll(pagination)
        this.tableData = res.data
        this.currentPage = res.pagination.pageNo
        this.pageSize = res.pagination.pageSize
        this.total = res.pagination.total
      } catch (error) {
        console.log(error)
      }

    },
  },

  mounted() {
    this.handlePageChange()
  }
};
</script>

<style scoped>

</style>

