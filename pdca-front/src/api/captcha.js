import http from '../utils/http'

export function captcha(params){
    return http({
        method: 'post',
        url: 'captcha',
        params,
        responseType: 'blob'  // 或 'arraybuffer'，根据实际情况选择
    })
}
