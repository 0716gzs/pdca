<template>
  <div>
    <el-button type="primary" @click="openDialog">添加</el-button>

    <el-dialog
        v-model="showDialog"
        title="添加表单"
        width="60%"
        @close="handleClose"
    >
      <div class="dialog-content">
        <el-form :model="formDataList" ref="form" label-width="120px">
          <div v-for="(formData, formDataIndex) in formDataList" :key="formDataIndex">
            <div v-for="(field, index) in fields" :key="index" class="form-group">
            <div v-if="field.type === 'text'">
              <el-form-item :label="field.label" :prop="field.name" style="margin-top: 20px">
                <el-input
                    v-if="field.type"
                    :id="field.name"
                    :name="field.name"
                    :clearable=true
                    v-model="formData[field.name]"
                    :placeholder="field.placeholder"
                />
              </el-form-item>
            </div>

            <div v-if="field.type === 'select'" style="margin-top: 25px">
              <el-form-item :label="field.label" :prop="field.name">
                <el-select
                    v-if="field.type"
                    :id="field.name"
                    :name="field.name"
                    :clearable=true
                    v-model="formData[field.name]"
                    :placeholder="field.placeholder"
                >

                  <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </div>


            <div class="block" v-if="field.type === 'datatime'">
              <div class="form-item-div">
                <el-form-item :label="field.label" :prop="field.name"></el-form-item>

              </div>

              <el-date-picker
                  v-model="formData[field.name]"
                  type="datetimerange"
                  range-separator="至"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期">
              </el-date-picker>
            </div>

          </div>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="handleClose">关闭</el-button>
            <el-button type="primary" @click="handleSubmit">提交</el-button>
            <el-button type="primary" @click="addField">添加</el-button>
          </div>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: 'DialogComponent',
  components: {
  },
  props: {
    fields: {
      type: Array,
      required: true
    },
    initialData: {
      type: Array,
      default: () => ({})
    },
    fields_length: {
      type: Number,
      required: true
    },
    submitText: {
      type: String,
      default: 'Submit'
    }
  },
  data() {
    return {
      showDialog: false,
      formDataList: [ ...this.initialData ],
      options: [{
        value: '1',
        label: '简单'
      }, {
        value: '2',
        label: '一般'
      }, {
        value: '3',
        label: '困难'
      }],
    };
  },
  methods: {
    init_data(){
      // 确保 formDataList 不为空，并使用第一个对象作为模板
      const template = this.formDataList.length > 0 ? this.formDataList[0] : {};

      // 创建一个新字段对象，根据模板动态生成
      const newInitialData = Object.keys(template).reduce((acc, key) => {
        acc[key] = ''; // 设置新字段的值为空字符串
        return acc;
      }, {});
      this.formDataList = [];
      // 添加新字段到 formDataList
      this.formDataList.push(newInitialData);
      console.log(this.formDataList)
    },
    handleSubmit() {
      this.$emit('submit', this.formDataList);
      this.showDialog = false;
    },
    handleClose() {
      this.showDialog = false;
      this.$emit('fields_list', this.fields);
    },
    openDialog() {
      this.showDialog = true;
      this.init_data()
    },
    addField(){
      let newFields = [...this.fields]
      for (let i = 0; i < newFields.length; i++){
        if (i < this.fields_length){
          break
        }
        this.fields.push(newFields[i])
      }

      // 确保 formDataList 不为空，并使用第一个对象作为模板
      const template = this.formDataList.length > 0 ? this.formDataList[0] : {};

      // 创建一个新字段对象，根据模板动态生成
      const newInitialData = Object.keys(template).reduce((acc, key) => {
        acc[key] = ''; // 设置新字段的值为空字符串
        return acc;
      }, {});

      // 添加新字段到 formDataList
      this.formDataList.push(newInitialData);
    },

  },
}
</script>

<style>
.dialog-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 90%;
}

.dialog-footer {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.form-group {
  width: 110%;
  max-width: 400px; /* You can adjust this value as needed */
}

.el-form-item {
  margin-bottom: 20px; /* Add some spacing between form items */
}

/*时间容器*/
.block {
  display: flex;
  align-items: center; /* Vertically align items in the center */
  gap: 10px; /* Adjust the space between form item and date picker */
}

.form-item-div {
  margin-bottom: -15px; /* Remove bottom margin to align with date picker */
  flex: 0 0 auto; /* Prevent form item from stretching */
}

.date-picker {
  flex: 1; /* Allow the date picker to take up remaining space */
}

</style>
