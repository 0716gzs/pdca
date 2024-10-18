<template>
  <div>
    <el-multi-select-dropdown v-model="selectedTaskAttributes"/>

    <!-- S 表格 A -->
    <elTable :columns="columns" :tableData="tableData" :footerSlot="footerSlot" :showPagination="showPagination" :pager="listPagination" :empty="empty" :showSelection="showSelection"
             @handleSizeChange="handleSizeChange" @handleCurrentChange="handleCurrentChange">

      <el-table-column slot="showSelection" width="88" label="全选" align="center" type="selection">
      </el-table-column>
      <!-- /全选 -->


      <el-table-column slot="footerSlot" label="操作" align="right" width="200">
        <template slot-scope="scope">
          <el-button type="text">按钮</el-button>
        </template>
      </el-table-column>
      <!-- /尾部 -->
    </elTable>
    <!-- E 表格 A -->


  </div>
</template>

<script>
import elTable from "/src/components/CommonTable.vue";
import elMultiSelectDropdown from "/src/components/MultiSelectDropdown.vue";
export default {
  name: "sell",
  components: { elTable , elMultiSelectDropdown},
  data () {
    return {
      empty: {
        img: "https://XXX.png",
        description: "暂无"
      },//缺省页
      showSelection: true, // 多选插槽
      footerSlot: true, // 尾部插槽
      columns: [
        { label: "编号", prop: "id", align: "left" },
        { label: "计划名称", prop: "name", align: "right" },
        { label: "任务等级", prop: "level", align: "right" },
        { label: "开始时间", prop: "start_time", align: "right" },
        { label: "结束时间", prop: "end_time", align: "right" },
      ],//列属性
      tableData: [], //表格数据
      showPagination: true, //是否分页
      listPagination: {
        current: 1,
        size: 10,
        totalCount: 0,
      },//分页

      selectedTaskAttributes: [], // 用于保存选中的任务属性
    };
  },
  mounted () {
    this._list();
  },
  methods: {
    /**
     * 列表
     */
    async _list () {
        const res = await this.$api.pdca.plan(null, 'get')
        this.tableData = res.data;
        this.listPagination.totalCount = res.pagination.total;
      },

    /**
     * 分页
     */
    handleSizeChange (val) {
      this.listPagination.size = val;
    },
    handleCurrentChange (val) {
      this.listPagination.current = val;
    },
  },
};
</script>

<style>

</style>