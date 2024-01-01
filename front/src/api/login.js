import http from '@/utils/http'

export function login(data){
    return http({
        method: 'post',
        url: 'user/login',
        data
    })
}

export function register(data){
    return http({
        method: 'post',
        url: 'user/register',
        data
    })
}

// 用户基本信息接口
export function info(){
    return http({
        method: 'get',
        url: 'user/info'
    })
}