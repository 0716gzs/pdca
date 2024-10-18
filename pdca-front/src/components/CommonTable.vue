<template>
  <div style="width: 1210px">
    <!-- S 表格 A -->
    <el-table
        stripe
        :data="tableData"
        :header-cell-style="{background:'#eef1f6',color:'#606266'}"
        @selection-change="selectionChange"
    >
      <template slot="empty">
        <div class="empty-cont">
          <img :src="mTable.img" alt="" />
          <span>{{ mTable.description }}</span>
        </div>
      </template>
      <!-- /缺省页 -->

      <slot v-if="showSelection" name="showSelection" />
      <!-- /多选插槽 -->

      <slot v-if="headerSlot" name="headerSlot" />
      <!-- /头部插槽 -->

      <template v-for="(item, index) in columns" :key="index">
        <el-table-column
            :prop="getProp(item.prop)"
            :label="item.label"
            :align="item.align"
            :width="item.width"
            :class="item.style"
            :formatter="item.formatter ? item.formatter : formatterValue"
        >
        </el-table-column>
      </template>
      <!-- /表格内容 -->

      <!-- 操作按钮列 -->
      <el-table-column label="操作" width="200">
        <template v-slot="scope">
          <el-button
              type="primary"
              size="small"
              @click="handleEdit(scope.row)"
          >
            编辑任务
          </el-button>
          <el-button
              type="danger"
              size="small"
              @click="handleDelete(scope.row)"
          >
            删除任务
          </el-button>
        </template>
      </el-table-column>
      <!-- /操作按钮列 -->

      <slot v-if="footerSlot" name="footerSlot" />
      <!-- /尾部插槽 -->
    </el-table>
    <!-- E 表格 A -->

    <!-- S 分页 B -->
    <el-pagination
        background
        style="text-align: right;"
        v-if="showPagination"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="pager.pageNo"
        :page-size="pager.pageSize"
        :total="pager.totalCount"
        layout="total, sizes, prev, pager, next, jumper"
    >
    </el-pagination>
    <!-- E 分页 B -->
  </div>
</template>

<script>
export default {
  name: "elementTable",
  props: {
    empty: Object, //缺省
    columns: Array, //表格的列
    tableData: Array, //表格的数据
    showSelection: { type: Boolean, default: false }, //是否显示多选
    pager: Object, //分页传值
    showPagination: { type: Boolean, default: false }, //是否显示分页
    headerSlot: { type: Boolean, default: false }, //是否显示头部插槽
    footerSlot: { type: Boolean, default: false }, //是否显示底部插槽
  },
  computed: {
    // 缺省页默认值
    mTable() {
      return Object.assign(
          {
            description: "暂无数据"
          },
          this.empty
      );
    }
  },
  methods: {
    /**当选择项发生变化时会触发该事件*/
    selectionChange(val) {
      this.$emit("selectionChange", val);
    },

    /**分页*/
    handleSizeChange(val) {
      this.$emit("handleSizeChange", val);
    },
    handleCurrentChange(val) {
      this.$emit("handleCurrentChange", val);
    },

    /**表格内容插槽*/
    formatterValue(row, column, cellValue) {
      // 处理嵌套对象的情况
      if (typeof row[column.property] === "object" && row[column.property] !== null) {
        // 假设你只关心 level.display
        return row[column.property].display || ""; // 返回 display 字段或空字符串
      }
      return cellValue; // 返回原始值
    },

    /** 获取 prop 值，兼容字符串和对象的情况 */
    getProp(prop) {
      if (typeof prop === "object" && prop !== null && !Array.isArray(prop)) {
        // 假设只处理一个键值对
        return Object.keys(prop)[0];
      }
      return prop; // 如果是字符串，直接返回该值
    },

    /** 处理修改事件 */
    handleEdit(row) {
      this.$emit("edit", row); // Emit edit event with row data
    },

    /** 处理删除事件 */
    handleDelete(row) {
      this.$emit("delete", row); // Emit delete event with row data
    }
  }
};
</script>

<style lang="scss" scoped>
/* 缺省页
          ---------------------------------------------------------------- */
.empty-cont {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 40px 0;

  > img {
    width: 20%;
    height: 20%;
  }

  span {
    font-size: 14px;
    line-height: 1.8;
  }
}
</style>
