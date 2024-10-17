<!--<template>-->
<!--  <div>-->
<!--    <div id="login_container"></div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: 'WxLoginComponent',-->
<!--  async mounted() {-->
<!--    try {-->
<!--      await this.loadScript('http://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js');-->
<!--      this.initializeWxLogin();-->
<!--    } catch (error) {-->
<!--      console.error('Error loading wxLogin script:', error);-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    loadScript(src) {-->
<!--      return new Promise((resolve, reject) => {-->
<!--        if (document.querySelector(`script[src="${src}"]`)) {-->
<!--          resolve(); // Script is already loaded-->
<!--          return;-->
<!--        }-->

<!--        const script = document.createElement('script');-->
<!--        script.src = src;-->
<!--        script.onload = () => resolve();-->
<!--        script.onerror = () => reject(new Error(`Failed to load script ${src}`));-->
<!--        document.head.appendChild(script);-->
<!--      });-->
<!--    },-->
<!--    initializeWxLogin() {-->
<!--      if (typeof WxLogin === 'undefined') {-->
<!--        console.error('WxLogin script not loaded.');-->
<!--        return;-->
<!--      }-->

<!--      const wxLoginConfig = {-->
<!--        self_redirect: true,-->
<!--        id: "login_container", // 登录按钮的容器 ID-->
<!--        appid: "wx7f369b4e5c153e95", // 替换为你的公众号 AppID-->
<!--        scope: "snsapi_base", // 你需要的权限范围-->
<!--        redirect_uri: encodeURIComponent("http://localhost:8000/wx_qrcode_callback"), // 替换为你的回调地址-->
<!--        // state: "random_state_string", // 可选的状态参数-->
<!--        // style: "", // 登录按钮样式（可选）-->
<!--        // href: "" // 登录按钮的链接（可选）-->
<!--      };-->
<!--      new WxLogin(wxLoginConfig);-->
<!--    },-->

<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 样式根据需要进行调整 */-->
<!--</style>-->



// CreateForm.vue
<template>
  <div>
    <h2>创建表单</h2>
    <form @submit.prevent="saveForm">
      <div v-for="(field, index) in fields" :key="index">
        <label>字段名: <input v-model="field.name" /></label>
        <label>标签: <input v-model="field.label" /></label>
        <label>类型:
          <select v-model="field.type">
            <option value="text">文本</option>
            <option value="number">数字</option>
          </select>
        </label>
        <button @click="removeField(index)">删除</button>
      </div>
      <button type="button" @click="addField">添加字段</button>
      <button type="submit">保存表单</button>
    </form>
  </div>
</template>

<script>

export default {
  data() {
    return {
      fields: [
        { name: '', label: '', type: 'text' },
        { name: '', label: '', type: 'text' }
      ],
      formKey: 'myForm'  // 这里可以使用动态表单键
    };
  },
  methods: {
    addField() {
      this.fields.push({ name: '', label: '', type: 'text' });
    },
    removeField(index) {
      this.fields.splice(index, 1);
    },
    saveForm() {
      console.log(this.fields)
      alert('表单结构已保存');
    }
  }
};
</script>

