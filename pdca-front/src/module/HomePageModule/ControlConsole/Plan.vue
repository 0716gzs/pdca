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
  </div>
</template>

<script>
import DialogComponent from '/src/components/DialogComponent.vue';

export default {
  components: {
    DialogComponent,
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
      ]
    };
  },
  created() {
    this.fields_length = this.fields.length
  },
  mounted() {
    this.getPlanData()
  },
  methods: {
    async getPlanData(data) {
      // alert('提交')
      const res = await this.$api.plan.get_plan()
      console.log(res)
    },
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
      // alert('提交')
      const res = await this.$api.plan.add_plan(data)
      console.log(res)
    },
    handleFormClose() {
      console.log('Form closed');
      // Handle form close
    }
  }
}
</script>
