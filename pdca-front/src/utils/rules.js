// 编写规则
export function registerRules (context) {
    return {
        nickname: [
            {
                required: true,
                message: '用户名是必传内容',
                // 失去焦点是判断是否符合要求规则
                trigger: 'blur'
            },
            {
                pattern: /^[a-z0-9]{3,10}$/,
                message: '用户名必须是3-10个字母或者数字',
                trigger: 'blur'
            }
        ],
        password: [
            {
                required: true,
                message: '密码是必传内容',
                // 失去焦点是判断是否符合要求规则
                trigger: 'blur'
            },
            {
                pattern: /^[a-z0-9]{3,}$/,
                message: '密码必须是3位以上的字母或者数字',
                trigger: 'blur'
            }
        ],
        verify_password: [
            {
                required: true,
                message: '请再次输入密码',
                trigger: 'blur'
            },
            {
                validator: (rule, value, callback) => {
                    if (value !== context.form.password) {
                        callback(new Error('两次输入的密码不一致'));
                    } else {
                        callback();
                    }
                },
                trigger: 'blur'
            }
        ],
        phone: [
            { required: true, message: '请输入手机号', trigger: 'blur' },
            { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
        ],
        code: [
            { required: true, message: '请输入验证码', trigger: 'blur' }
        ]
    }
}


export function registerPhoneRules () {
    return {
        phone: [
            { required: true, message: '请输入手机号', trigger: 'blur' },
            { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
        ],
        code: [
            { required: true, message: '请输入验证码', trigger: 'blur' }
        ]
    }
}

export function LoginAccountRules() {
    return {
        account_email: [
            {
                required: true,
                message: '账号或邮箱是必传内容',
                trigger: 'blur'
            },
            {
                validator: (rule, value, callback) => {
                    const accountPattern = /^[a-zA-Z0-9]{6,10}$/;
                    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

                    if (accountPattern.test(value)) {
                        callback(); // 账号格式正确
                    } else if (emailPattern.test(value)) {
                        callback(); // 邮箱格式正确
                    } else {
                        callback(new Error('账号必须是6-10位字母或数字，或有效的邮箱地址'));
                    }
                },
                trigger: 'blur'
            }
        ],
        password: [
            {
                required: true,
                message: '密码是必传内容',
                trigger: 'blur'
            },
            {
                pattern: /^[a-z0-9]{3,}$/,
                message: '密码必须是3位以上的字母或者数字',
                trigger: 'blur'
            }
        ],
    }
}