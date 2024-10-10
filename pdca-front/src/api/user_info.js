import http from '../utils/http'
import {removeCookie, setCookie, getCookie, RemoveStorage} from '/src/utils/token'

export function getUserInfo(){
    return http({
        method: 'get',
        url: 'user/info',
    })
}

let promise;
// 原始的 refreshToken 函数
export async function refreshToken() {
    if (promise){
        return promise;
    }else{
        promise = new Promise(async (resolve, reject) =>{
            const resp = await http({
                method: 'get',
                url: 'refresh/token',
                params: {
                    refresh_token: getCookie('refresh_token')
                },
                __isRefreshToken: true,
            });
            removeCookie('user_token')
            removeCookie('refresh_token')
            setCookie('user_token', resp.user_token)
            setCookie('refresh_token', resp.refresh_token)

            resolve(resp.code === 200);
        })
    }

    promise.finally(()=>{
        promise = null;
    });
    return promise
}

export function getUserInfoByToken(config){
    return !!config.__isRefreshToken;
}