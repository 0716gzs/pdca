import http from '../utils/http'

export function SendCode(data){
    return http({
        method: 'post',
        url: 'user/SendCode',
        data
    })
}

export function GetAuthUrl(params){
    return http({
        method: 'get',
        url: 'GetAuthUrl',
        params
    })
}
