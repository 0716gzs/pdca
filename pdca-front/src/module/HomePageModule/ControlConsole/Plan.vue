<template>
  <div>
    <dialog-component
        :fields="fields"
        :initialData="initialData"
        :fields_length="fields_length"
        @submit="handleFormSubmit"
        @fields_list="init_fields_list"
        @close="handleFormClose"
    />

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
import DialogComponent from '/src/components/DialogComponent.vue';
import elTable from "/src/components/CommonTable.vue";

export default {
  components: {
    DialogComponent,
    elTable
  },
  data() {
    return {
      fields: [
        { name: 'name', label: '计划', type: 'text', placeholder: '请输入您的计划'},
        { name: 'level', label: '等级', type: 'select', placeholder: '请选择计划等级'},
        { name: 'datatime', label: '时间', type: 'datatime', placeholder: ''},
        // Add more fields as needed
      ],
      fields_length: 0,
      initialData: [
        {
          name: '',
          level: '',
          datatime: '',
        }
      ],
      // 表格数据
      empty: {
        img: "https://XXX.png",
        description: "暂无"
      },//缺省页
      showSelection: true, // 多选插槽
      footerSlot: true, // 尾部插槽
      columns: [
        { label: "编号", prop: "id", align: "center", width: 100 },
        { label: "计划名称", prop: "name", align: "center", width: 200 },
        { label: "任务等级", prop: "level", align: "center", width: 200 },
        { label: "开始时间", prop: "start_time", align: "center", width: 200 },
        { label: "结束时间", prop: "end_time", align: "center"},
      ],//列属性
      tableData: [], //表格数据
      showPagination: true, //是否分页
      listPagination: {
        current: 1,
        size: 10,
        totalCount: 0,
      },//分页

    };
  },
  created() {
    this.fields_length = this.fields.length
  },
  methods: {
    init_fields_list(data){
      this.fields = []
      for(let i = 0; i < data.length; i++){
        if (i < this.fields_length){
          this.fields.push(data[i])
        }else{
          break
        }
      }
    },
    async handleFormSubmit(data) {
      const res = await this.$api.pdca.plan(data)
      this.$router.go(0); // 使用 go(0) 刷新当前路由
      // Handle form submission
    },
    handleFormClose() {
      console.log('Form closed');
      // Handle form close
    },

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
  mounted () {
    this._list();
  },
}
</script>
