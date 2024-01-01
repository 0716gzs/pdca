import Vue from "vue";
import VueRouter from "vue-router";
import {GetStorage} from "@/utils/token";
import {decrypt} from "@/utils/utls";

Vue.use(VueRouter);

const routes = [
    // {
    //     path: '/',
    //     redirect: '/',
    // },
    {
        path: '/',
        component: () => import("@/components/views/home_page/HomePages.vue"),
    },
    {
        path: '/index',
        component: () => import("@/components/views/home_page/index.vue"),
    },
    {
        path: '/home',
        component: () => import("@/components/views/home_page/Home.vue"),
    },
    //登录
    {
        path: "/login",
        name: "login",
        component: () => import("@/components/views/login/login.vue"),
    },
    // 注册账号
    {
        path: "/Register",
        name: "Register",
        component: () => import("@/components/views/login/Register.vue"),
    },
    // 注册成功页面
    {
        path: "/success_response",
        name: "success_response",
        component: () => import("@/components/views/login/success_response.vue"),
    },
    // 忘记密码
    {
        path: "/ForgotPassword",
        name: "ForgotPassword",
        component: () => import("@/components/views/login/ForgotPassword.vue"),
    },
    // 用户中心
    {
        path: "/user_info",
        name: "UserInfo",
        component: () => import("@/components/views/userinfo/UserInfo.vue"),
    },


    {
        path: '/index',
        name: "index",
        component: () => import("@/components/views/home_page/index.vue"),
        children:[
            {path: '/index/BugManage',component: () => import('@/components/views/resources/projects/BugManage.vue')},
            {path: '/index/ProjectManage',component: () => import('@/components/views/resources/projects/ProjectManage.vue')},
            {path: '/index/ConfMysql',component: () => import('@/components/views/resources/ConfMysql.vue')},
            {path: '/index/ConfMongo',component: () => import('@/components/views/resources/ConfMongo.vue')},
            {path: '/index/ConfRedis',component: () => import('@/components/views/resources/ConfRedis.vue')},
            {path: '/index/AddUser',component: () => import('@/components/views/resources/User_conf/AddUser.vue')},
            {path: '/index/AddRole',component: () => import('@/components/views/resources/User_conf/AddRole.vue')},
            {path: '/index/AddResources',component: () => import('@/components/views/resources/User_conf/AddResources.vue')},
        ]
    },


];

const router = new VueRouter({
    routes,
});

// var white = ['/index', '/login', 'ForgotPassword', 'success_response', 'Register']
router.beforeEach((to, from, next) => {
    next()
    // //设置所有人都能访问的页面白名单
    // let white = ['/', '/index', '/login', '/ForgotPassword', '/success_response', '/Register', '/home']
    // //取出用户登录存储的资源权限
    // if(GetStorage('ResourceList')){
    //     var pathlist = JSON.parse(decrypt(GetStorage('ResourceList')))
    // }
    //
    // //判断是否有用户登录存储的资源权限
    // if(pathlist){
    //     //加入白名单
    //     for(var i=0;i<=pathlist.length;i++){
    //         white.push(pathlist[i])
    //     }
    //     //判断访问路径是否在白名单内
    //     if(white.includes(to.path)){
    //         next()
    //     }else{
    //         alert("您没有权限1")
    //     }
    // }else {
    //     if (white.includes(to.path)) {
    //         next()
    //     } else {
    //         alert("您没有权限2")
    //     }
    // }
})



export default router;
