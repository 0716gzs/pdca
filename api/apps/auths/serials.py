from rest_framework.fields import IntegerField
from rest_framework.serializers import SerializerMethodField
from apps.auths.models import *
from common.serials import BaseSerializer


class UserSimpleSerial(BaseSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname')


class RoleSimpleSerial(BaseSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')


class DepartmentSimpleSerial(BaseSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class DepartmentSerial(BaseSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class UserRoleSerial(BaseSerializer):
    role = RoleSimpleSerial()

    class Meta:
        model = UserRole
        fields = ('id', 'role')


class UserDepartmentSerial(BaseSerializer):
    department = DepartmentSimpleSerial()

    class Meta:
        model = UserDepartment
        fields = ('id', 'department')


class UserEditSerial(BaseSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'mobile', 'email', 'username', 'avatar', 'password', 'enable')


class UserDetailSerial(BaseSerializer):
    role_user = UserRoleSerial(many=True)
    department_user = UserDepartmentSerial(many=True)
    roles = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'nickname', 'mobile', 'email', 'avatar', 'username', 'last_login', 'expire_time', 'enable',
            'update_time', 'create_time', 'role_user', 'roles', 'department_user')

    def get_roles(self, obj):
        return [r.role.name for r in obj.role_user.all()]


class RoleEditSerial(BaseSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')


class RoleSerial(BaseSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')


class UserRolesSimpleSerial(BaseSerializer):
    role_user = UserRoleSerial(many=True)

    class Meta:
        model = User
        fields = ('id', 'nickname', 'role_user', 'mobile', 'email')


class UserRoleDepartmentSimpleSerial(BaseSerializer):
    role_user = UserRoleSerial(many=True)
    department_user = UserDepartmentSerial(many=True)

    class Meta:
        model = User
        fields = ('id', 'nickname', 'role_user', 'department_user')


class DepartmentEditSerial(BaseSerializer):
    class Meta:
        model = Department
        fields = ('id', 'parent', 'name')


class DepartmentDetailSerial(BaseSerializer):
    user_count = IntegerField()

    class Meta:
        model = Department
        fields = ('id', 'parent_id', 'name', 'user_count')


class UserDepartmentDetailSerial(BaseSerializer):
    user = UserRolesSimpleSerial()

    class Meta:
        model = UserDepartment
        fields = ('id', 'user', 'department')


class UserDepartmentEditSerial(BaseSerializer):
    class Meta:
        model = UserDepartment
        fields = ('id', 'user', 'department')
