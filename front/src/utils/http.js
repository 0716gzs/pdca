import axios from "axios";
import {GetStorage} from '@/utils/token'
import status from '@/utils/status'

let baseURL = "http://127.0.0.1:8000/api/v1/";


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
    if (GetStorage('UserToken')) {
        config.headers.Authorization = 'Bearer ' + GetStorage('UserToken');
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
        return res.data;
    },
    (error) => {
        // return status(error)
        return status(error.response.data.code, error.response.data.message, error.response.data.success)
    }
);
export default server;

// sudo cp /etc/apt/sources.list  /etc/apt/sources.list.bak_1
//cd /etc/apt
//  vi sources.list

