from django.db.models import Q, F
from django.forms import BooleanField
from rest_framework.serializers import CharField
from apps.auths.serials import *
from apps.auths.service import AccountService
from common.views import PermLessApiView, BaseParam, BaseModelViewSet, RowDict
from apps.auths.models import *
# from common.zf.wechatpayv3.qrcode import get_qrcode_wx_url
from verify.verify_method import account_email_check


class LoginView(PermLessApiView):
    """登录"""

    class RegisterParam(BaseParam):
        account_email = CharField(required=False, help_text='账号/邮箱')
        password = CharField(required=False, help_text='登陆密码')
        login_user_agreed = BooleanField(required=True, help_text='用户协议')

    def post(self, request):
        # _Param 中的参数和前端传入的request.data参数进行校验
        requ_form = RowDict(request.data)
        requ_form = account_email_check(requ_form)
        user_info = User.objects.get_or_none(Q(account=requ_form.account_email) | Q(email=requ_form.account_number))

        if not user_info:
            return self.fail_response('用户名不存在')

        if not user_info.check_password(requ_form.password):
            return self.fail_response('密码错误')

        if user_info.disabled():
            return self.fail_response('账号已禁用')
        user_info.save()

        data = UserSimpleSerial(user_info).data
        data['token'] = AccountService.get_login_token(user_info)
        data['refresh_token'] = AccountService.get_login_token_refresh_token(user_info)
        return self.success_response(data)


# class WxLoginView(PermLessApiView):
#     """微信登录"""
#
#     class WxLoginParam(BaseParam):
#         secret_key = CharField(required=True, help_text='密钥用于获取微信登陆二维码')
#
#     def get(self, request):
#         # _Param 中的参数和前端传入的request.data参数进行校验
#         param = self.valid_param(self.WxLoginParam(data=request.query_params))
#         url = get_qrcode_wx_url()
#         # 校验密钥是否正确secret_key
#         resp = {
#             'auth_url': url
#         }
#         return self.success_response(resp)
#
#
# class WxLoginCallbackView(PermLessApiView):
#     """微信登录"""
#
#     def get(self, request):
#         print(request)
