import re
from common.exceptions import ParamError
from common.views import RowDict
from common.redis_client import RedisClient


def verifyPhone(phone):
    if not phone:
        raise ParamError('手机号不能为空，请重新输入')
    # pattern = r'^1[3456789]\d{9}$'
    pattern = r'^1[3-9]\d{9}$'
    match = re.match(pattern, phone)
    if not match:
        raise ParamError('手机号格式不正确，请重新输入')


def register_check(login_param: RowDict, is_pwd):
    if login_param.user_agreed is not True:
        raise ParamError('请同意用户协议')
    if is_pwd:
        if login_param.password != login_param.verify_password:
            raise ParamError('两次密码不一致')

    verifyPhone(login_param.phone)
    redis_code = RedisClient.get_str(login_param.phone)
    if not redis_code:
        raise ParamError("验证码已失效")
    pattern = r'^\d+$'
    if not re.match(pattern, login_param.code) or len(login_param.code) > 4:
        raise ParamError("验证码不合法，请重新输入")
    if int(login_param.code) != int(redis_code):
        raise ParamError("验证码不正确，请重新输入")


def captcha_check(param, valid_param):
    redis_img_msg = str(RedisClient.get_str(param.uuid))
    if not redis_img_msg:
        raise ParamError("请填写验证码")
    if param.img_code.lower() != redis_img_msg.lower():
        raise ParamError("图形验证码错误")

    verifyPhone(param.phone)


def verify_login_user_agreed(user_agreed):
    if not user_agreed:
        raise ParamError('请同意用户协议')


def account_email_check(requ_form):
    verify_login_user_agreed(requ_form.login_user_agreed)

    return requ_form

