import http from '../utils/http'


export function register(data){
    return http({
        method: 'post',
        url: 'user/register',
        data
    })
}
