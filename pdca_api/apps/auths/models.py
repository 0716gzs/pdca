import datetime

from django.contrib.auth.hashers import (
    check_password, make_password
)
from django.db import models

from common.fields import FileIdField
from common.fields import SimpleForeignKey
from common.models import BaseModel


class User(BaseModel):
    """
  `account` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL COMMENT '账号',

    """
    nickname = models.CharField(max_length=64, default='', null=True, blank=True, help_text='账号名')
    account = models.CharField(max_length=10, default=None, help_text='账号ID')
    phone = models.CharField(max_length=11, default='', blank=True, help_text='手机号')
    email = models.CharField(max_length=32, default='', blank=True, help_text='邮箱')
    avatar = FileIdField(help_text='头像', default='', blank=True)
    password = models.CharField(max_length=128, default='')
    last_login = models.DateTimeField(default=None, null=True, blank=True, help_text='最近登录时间')
    enable = models.BooleanField(default=True, help_text='是否启用')

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息'

    @staticmethod
    def mk_password(raw_password):
        return make_password(raw_password)

    def role_names(self):
        return [ur.role.name for ur in UserRole.objects.filter(user_id=self.id)]

    def roles(self):
        return [ur.role for ur in UserRole.objects.filter(user_id=self.id) if ur.role]

    def set_password(self, raw_password):
        self.password = self.mk_password(raw_password)

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        return check_password(raw_password, self.password)

    def disabled(self):
        return not self.enable


class Role(BaseModel):
    name = models.CharField(max_length=32, default='', help_text='角色名称')
    description = models.CharField(max_length=32, default='', help_text='角色名称')
#
    class Meta:
        db_table = 'role'
        verbose_name = verbose_name_plural = '角色信息'


class UserRole(BaseModel):
    user = SimpleForeignKey('auths.User', related_name='role_user')
    role = SimpleForeignKey('auths.Role', related_name='user_role')

    class Meta:
        db_table = 'user_role'
        verbose_name = verbose_name_plural = '用户角色'


class Department(BaseModel):
    parent = SimpleForeignKey('self', null=True, blank=True, help_text='父节点')
    name = models.CharField(max_length=255, default='', help_text='节点名称')

    class Meta:
        db_table = 'department'
        verbose_name = verbose_name_plural = '部门'


class UserDepartment(BaseModel):
    user = SimpleForeignKey('User', related_name='department_user')
    department = SimpleForeignKey('Department', related_name='user_department')

    class Meta:
        db_table = 'user_department'
        verbose_name = verbose_name_plural = '用户部门'
