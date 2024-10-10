from django.forms import BooleanField
from rest_framework.serializers import CharField

from apps.auths.serials import UserSimpleSerial
from apps.auths.service import AccountService
from common.views import PermLessApiView, BaseParam, RowDict
from apps.auths.models import *
from verify.verify_method import register_check


class RegisterView(PermLessApiView):
    class RegisterParam(BaseParam):
        nickname = CharField(required=False, help_text='登录名')
        password = CharField(required=False, help_text='登陆密码')
        verify_password = CharField(required=False, help_text='登陆密码')
        phone = CharField(required=True, help_text='手机号')
        code = CharField(required=True, help_text='验证码')
        user_agreed = BooleanField(required=True, help_text='用户协议')

    def post(self, request):
        # _Param 中的参数和前端传入的request.data参数进行校验
        register_param = RowDict(self.valid_param(self.RegisterParam(data=request.data)))
        register_param.user_agreed = request.data.get('user_agreed')
        register = False
        if not register_param.nickname and not register_param.password \
                and not register_param.verify_password:
            # 手机号注册
            register_check(register_param, is_pwd=False)
            # 检查手机号是否以及注册
            register = User.objects.get_or_none(phone=register_param.phone)
            register = register if register else False
        else:
            # 账号密码注册
            register_check(register_param, is_pwd=True)
            # 查询该账号是否注册
            user_params = User.objects.get_or_none(phone=register_param.phone)
            if user_params:
                return self.fail_response(msg='手机号已被注册')

        # 生成账号
        if register is False:
            account = AccountService.generate()
            user_account = User.objects.get_or_none(account=account)
            if user_account:
                account = AccountService.generate()

            register = User(
                account=account,
                nickname=register_param.nickname,
                password=register_param.password,
                phone=register_param.phone,
            )
            register.set_password(register.password)
            register.save()
        # 生成token 默认登陆
        data = UserSimpleSerial(register).data
        data['token'] = AccountService.get_login_token(register)
        data['refresh_token'] = AccountService.get_login_token_refresh_token(register)
        return self.success_response(data)
