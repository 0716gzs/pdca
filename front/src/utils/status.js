import { Message } from 'element-ui';
import router from '@/router'

export default function status(res, msg, success){
    switch (res){
        case 0:
            Message.error(msg);
            break;
        case 100:
            Message.error(msg);
            break;
        case 200:
            Message.success(msg);
            break;
        case 300:
            Message.error(msg);
            break;
        case 400:
            router.push('/404')
            Message.error(msg);
            break;
        case 500:
            router.push('/500')
            Message.error(msg);
            break;
    }
    if (success){
        return success
    }else{
        throw ''
    }
}
