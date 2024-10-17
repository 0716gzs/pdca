from rest_framework.fields import IntegerField
from rest_framework.serializers import SerializerMethodField
from apps.auths.models import *
from common.serials import BaseSerializer


class UserSimpleSerial(BaseSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'account', 'phone', 'email', 'avatar', 'enable')


class UserEditSerial(BaseSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'mobile', 'email', 'username', 'avatar', 'password', 'enable')


class UserDetailSerial(BaseSerializer):
    # role_user = UserRoleSerial(many=True)
    # department_user = UserDepartmentSerial(many=True)
    roles = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'nickname', 'mobile', 'email', 'avatar', 'username', 'last_login', 'expire_time', 'enable',
            'update_time', 'create_time', 'role_user', 'roles', 'department_user')

    def get_roles(self, obj):
        return [r.role.name for r in obj.role_user.all()]

