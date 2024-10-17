import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import {router} from './router'; // 导入路由对象
import API from './api' // 导入请求
import status from './utils/status' // 导入状态
import footerDirective from './module/public/footer/footer'; // 底部

// 导入element element-plus
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

// 如果您正在使用CDN引入，请删除下面一行。
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


const app = createApp(App);
app.use(router); // 使用路由对象
app.use(ElementPlus);
app.directive('footer', footerDirective);

app.config.productionTip = false
app.config.globalProperties.$api = API;//请求接口api
app.config.globalProperties.$status = status; // 设置全局属性 $status

// 注册图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.mount('#app');
