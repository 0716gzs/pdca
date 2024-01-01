from django.db.models import Q, F
from rest_framework.serializers import CharField
from apps.auths.serials import *
from apps.auths.service import AccountService
from common.views import PermLessApiView, BaseParam, BaseModelViewSet
from apps.auths.models import *


class LoginView(PermLessApiView):
    """后台登录"""

    class _Param(BaseParam):
        account_number = CharField(required=True, help_text='账号')
        password = CharField(required=True, help_text='密码')

    def post(self, request):
        # _Param 中的参数和前端传入的request.data参数进行校验
        auth_param = self.valid_param(self._Param(data=request.data))
        account = User.objects.get_or_none(Q(account=auth_param.account_number) | Q(username=auth_param.account_number))

        if not account:
            return self.fail_response('用户名不存在')

        if not account.check_password(auth_param.password):
            return self.fail_response('密码错误')

        if account.disabled():
            return self.fail_response('账号已禁用')

        if account.expired():
            return self.fail_response('账号已过期')

        account.last_login = datetime.datetime.now()
        account.save()

        data = UserSimpleSerial(account).data
        data['token'] = AccountService.get_login_token(account)
        return self.success_response(data)


class RegisterView(PermLessApiView):
    class RegisterParam(BaseParam):
        username = CharField(required=True, help_text='用户名')
        password = CharField(required=True, help_text='密码')

    def post(self, request):
        # _Param 中的参数和前端传入的request.data参数进行校验
        register_param = self.valid_param(self.RegisterParam(data=request.data))
        # 生成账号
        account_number = AccountService.generate()
        account = User.objects.get_or_none(account=account_number)
        if account:
            account_number = AccountService.generate()
        else:
            register = User(
                account=account_number,
                username=register_param.username,
                password=register_param.password,
            )
            register.set_password(register.password)
            register.save()
        return self.success_response(data={'account_number': account_number})
