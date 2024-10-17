// 创建一个方法来封装表单验证逻辑
export function refsForm(context) {
    console.log(context.$refs)
    return new Promise((resolve, reject) => {
        context.$refs.form.validate((valid) => {
            resolve(valid);
        });
    });
}