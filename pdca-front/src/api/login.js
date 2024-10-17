import http from '../utils/http'

export function login(data){
    return http({
        method: 'post',
        url: 'user/login',
        data
    })
}
