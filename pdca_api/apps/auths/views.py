from common.views import BaseApiView, BaseParam, PermLessApiView, RowDict
from rest_framework.serializers import CharField
from apps.auths.serials import *
from apps.auths.service import *
from django.http import HttpResponse
from common.redis_client import RedisClient
from common.captcha.captcha import captcha
from verify.verify_method import captcha_check


class CaptchaView(PermLessApiView):
    class _Param(BaseParam):
        uuid = CharField(required=True, help_text='uuid')

    def post(self, request):
        param = self.valid_param(self._Param(data=request.query_params))
        # 导用cpatcha  text是图片验证码中数字 img是字节流
        name, text, img = captcha.generate_captcha()
        print(text)
        # 保存图形验码
        RedisClient.set_str(param.uuid, text, 300)  # set中前一个参数是键 后一个参数是值
        return HttpResponse(img, content_type='image/jpg')


class SendCodeView(PermLessApiView):
    """发送验证码"""

    class _Param(BaseParam):
        phone = CharField(required=True, help_text='手机号')
        uuid = CharField(required=True, help_text='uuid')
        img_code = CharField(required=True, help_text='img_code')

    def post(self, request):
        # _Param 中的参数和前端传入的request.data参数进行校验
        param = self.valid_param(self._Param(data=request.data))
        captcha_check(param, self.valid_param)
        code = random.randint(1000, 9999)
        # 腾讯云
        # try:
        #     Sample().main(param.phone, str(code))
        #     # 发送验证码后存入redis
        #     cache.set(str(param.phone), code)
        #     cache.expire(str(param.phone), 60)
        #     return self.success_response(message='发送成功')
        # except Exception as e:
        #     return self.fail_response(f'发送失败{e}')
        res = 1
        if res:
            # 发送验证码后存入redis
            RedisClient.set_str(str(param.phone), code, 120)
            return self.success_response(code, message='发送成功')
        else:
            return self.fail_response('发送失败')


class UserProfileView(BaseApiView):
    """个人信息"""

    def get(self, request):
        user = User.objects.get_or_none(pk=request.user_id)
        data = UserSimpleSerial(user).data
        return self.success_response(data)

    def post(self, request):
        param = self.valid_param(self._Param(data=request.data))
        account = User.objects.get_or_none(pk=request.user_id)

        if param.avatar:
            account.avatar = param.avatar

        if param.name:
            account.nickname = param.nickname

        account.save()
        data = UserDetailSerial(account).data
        return self.success_response(data)


class RefreshToken(BaseApiView):
    """获取刷新token"""

    def get(self, request):
        params = RowDict(request.query_params)
        params.refresh_token = params.refresh_token if type(params.refresh_token) is str else str(params.refresh_token[0])
        payload = AccountService.get_login_token_payload(params.refresh_token, verify=False)
        params.id = payload.user_id
        data = dict()
        data['user_token'] = AccountService.get_login_token(params)
        data['refresh_token'] = AccountService.get_login_token_refresh_token(params)
        data['code'] = int(200)
        return self.success_response(data)
