import Vue from 'vue'
import App from './App.vue'
import router from './router'
import API from './api'
import status from './utils/status'

Vue.config.productionTip = false

Vue.prototype.$api = API;//请求接口api
Vue.prototype.$status = status;//请求接口api




//全局引入vant
import Vant from 'vant';
import 'vant/lib/index.css';
Vue.use(Vant);


//全局引入element ui
import ElementUI from 'element-ui'
// 加载 element 组件库的样式
import 'element-ui/lib/theme-chalk/index.css'
// 全局注册 element 组件库
Vue.use(ElementUI)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
