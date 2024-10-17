// DynamicForm.vue
<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div v-for="(field, index) in formFields" :key="index">
        <label :for="field.name">{{ field.label }}</label>
        <input v-if="field.type === 'text'" :type="field.type" :name="field.name" v-model="formData[field.name]" />
        <input v-if="field.type === 'number'" :type="field.type" :name="field.name" v-model="formData[field.name]" />
        <!-- 你可以根据需要添加更多的字段类型 -->
      </div>
      <button type="submit">提交</button>
    </form>
  </div>
</template>

<script>
export default {
  props: {
    formFields: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      formData: {}
    };
  },
  methods: {
    handleSubmit() {
      this.$emit('submit', this.formData);
    }
  },
  watch: {
    formFields: {
      immediate: true,
      handler(newFields) {
        this.formData = {};
        newFields.forEach(field => {
          this.$set(this.formData, field.name, '');
        });
      }
    }
  }
};
</script>

