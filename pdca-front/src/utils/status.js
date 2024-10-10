import { ElMessage } from 'element-plus'
import { router } from '../router'

export default function status(res, msg, success){
    switch (res){
        case 0:
            ElMessage.error(msg);
            break;
        case 100:
            ElMessage.error(msg);
            break;
        case 200:
            ElMessage.success(msg);
            break;
        case 300:
            ElMessage.error(msg);
            break;
        case 400:
            ElMessage.error(msg);
            break;
        case 500:
            ElMessage.error(msg);
            break;
    }
    if (success){
        return success
    }else{
        throw ''
    }
}
