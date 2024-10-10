import http from '../utils/http'

export function add_plan(data){
    return http({
        method: 'post',
        url: 'plan',
        data
    })
}

export function get_plan(){
    return http({
        method: 'get',
        url: 'plan',
    })
}
