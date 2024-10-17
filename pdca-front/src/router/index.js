import {createRouter, createWebHistory} from "vue-router";

// const pages = import.meta.glob('../views/**/*page.js', { eager: false });
const pages = import.meta.glob('../views/**/*/page.js', {
   eager: true,
   import: 'default',
});

const components = import.meta.glob('../views/**/index.vue', {
   eager: true,
   import: 'default',
});

const routes = Object.entries(pages).map(([path, meta]) => {
   const compPath = path.replace('page.js', 'index.vue');
   path = path.replace('../views', '').replace('/page.js',
       '') || '/';
   const name = path.split('/').filter(Boolean).join('-') || 'index'

   return {
      path,
      name,
      component: components[compPath],
      meta,
   }
})

// 添加重定向规则
routes.unshift({
   path: '/',
   redirect: '/HomePage', // 访问根路径时重定向到 /astral
});

export const router = createRouter({
   history: createWebHistory(),
   routes,
});