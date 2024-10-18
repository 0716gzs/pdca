import http from '../../utils/http';

export function plan(data, type) {
    return http({
        method: type === 'post' ? 'post' : type === 'get' ? 'get' : type === 'put' ? 'put' : type === 'delete' ? 'delete' : 'post', // 默认值为 'post'
        url: 'plan',
        data: type === 'get' || type === 'delete' ? undefined : data // GET 和 DELETE 不传入 data
    });
}
