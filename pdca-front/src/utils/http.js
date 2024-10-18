import axios from "axios";
import {getCookie, removeCookie, RemoveStorage} from './token'
import status from './status'
import { refreshToken, getUserInfoByToken } from '/src/api/user_info'
import { router } from '/src/router'; // 导入你的路由设置

let baseURL = "https://pdca.0716gzs.cn/pdca/";
// let baseURL = "http://127.0.0.1:8000/pdca";


const server = axios.create({
    baseURL,
    timeout: 8000,
    /* headers: {
      "content-Type": "application/json;charset=utf-8",
    }, */
});
// 请求拦截
server.interceptors.request.use((config) => {
    config.headers = config.headers || {};
    if (getUserInfoByToken(config)){
        config.headers.Authorization = 'Bearer ' + getCookie('refresh_token');
    }else if (getCookie('user_token')) {
        config.headers.Authorization = 'Bearer ' + getCookie('user_token');
    }else {
        console.log('未登录')
        // router.push({path: '/login'})
    }
    // 进度条
    // nprogress.start();
    return config;
});

// 响应拦截
/**
 * 请求失败后的错误统一处理
 * @param {Number} status 请求失败的状态码
 */
server.interceptors.response.use(
    (res) => {
        // 进度条
        // nprogress.done();
        res.data['code'] = res.status
        if (res.data instanceof Blob){
            return res.data;
        }
        if (res.data.pagination){
            return res.data;
        }
        return res.data.data;
    },
    async (error) => {
        // return status(error)
        if (error.response.data.code === 401 && !getUserInfoByToken(error.config)){
            // 刷新token
            const isSuccess = await refreshToken(); // 尝试刷新 token
            if (isSuccess){
                // 修改原来配置的headers
                error.config.headers.Authorization = `Bearer ${getCookie('user_token')}`
                //重新的token重新请求
                await server.request(error.config)
            }
        }else{
            const currentPath = window.location.pathname; // 获取当前路由路径
            // 如果访问的是需要认证的页面且未登录，则重定向到登录页面
            if (currentPath !== '/HomePage') {
                removeCookie('user_token');
                RemoveStorage('user_data');
                RemoveStorage('menu_index');
                removeCookie('refresh_token');
                router.push({ path: '/login' });
            }
        }
        return status(error.response.data.code, error.response.data.message, error.response.data.success)
    }
);
export default server;

// sudo cp /etc/apt/sources.list  /etc/apt/sources.list.bak_1
//cd /etc/apt
//  vi sources.list

