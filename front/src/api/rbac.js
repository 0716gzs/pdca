import http from '@/utils/http'

export function getUserAll(params){
    return http({
        method: 'get',
        url: 'user/getUserAll',
        params
    })
}