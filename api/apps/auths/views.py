from apps.auths.models import *
from common.views import BaseModelViewSet, BaseApiView, BaseParam
from rest_framework.serializers import CharField, IntegerField
from apps.auths.serials import *
from apps.auths.service import *


class UserProfileView(BaseApiView):
    """个人信息"""
    class _Param(BaseParam):
        department = IntegerField(required=False)
        avatar = CharField(required=False)

    def get(self, request):
        user = User.objects.get_or_none(pk=request.user_id)
        data = UserDetailSerial(user).data
        resources_list = list()
        for i in data['role_user']:
            if not i['role']['resources_role']:
                continue
            else:
                for j in i['role']['resources_role']:
                    resources_list.append(j['resources'])
        resources_list = Tree.xtree(resources_list)
        data['resources_list'] = resources_list
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
