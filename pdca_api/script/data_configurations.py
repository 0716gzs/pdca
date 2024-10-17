import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *
from apps.auths.service import *
import random


def init_user():
    for i in range(3):
        account = AccountService.generate()
        user, _ = User.objects.get_or_create(username=random.randint(0, 10000), account=account)
        user.set_password('wowangle')
        user.save()


def init_role():
    role_list = [{'role_name': 'ADMIN *', 'role_description': '超级管理员'},
                 {'role_name': 'DC', 'role_description': '董事'},
                 {'role_name': 'GM', 'role_description': '总经理'},
                 {'role_name': 'DGM', 'role_description': '副总经理'},
                 {'role_name': 'PM', 'role_description': '项目经理'},
                 {'role_name': 'MG', 'role_description': '主管'},
                 {'role_name': 'BD', 'role_description': '后端开发'},
                 {'role_name': 'FD', 'role_description': '前端'},
                 {'role_name': 'TEST', 'role_description': '测试'},
                 {'role_name': 'OAM', 'role_description': '运维'},
                 {'role_name': 'HR', 'role_description': '人事'}]
    for i in role_list:
        role, _ = Role.objects.get_or_create(name=i['role_name'], description=i['role_description'])
        role.save()


def init_resources():
    resources_list = [
        {'name': '', 'description': '用户管理', 'tree_level': 0},
        {'name': '/AddUser', 'description': '添加用户', 'tree_level': 0},
        {'name': '/AddRole', 'description': '添加角色', 'tree_level': 0},
        {'name': '/AddResources', 'description': '添加资源url', 'tree_level': 0},
        {'name': '', 'description': '项目', 'tree_level': 0},
        {'name': '/ProjectManage', 'description': '项目管理', 'tree_level': 0},
        {'name': '/BugManage', 'description': 'Bug管理', 'tree_level': 0},
        {'name': '', 'description': '配置管理', 'tree_level': 0},
        {'name': '/ConfMysql', 'description': 'mysql配置', 'tree_level': 6},
        {'name': '/ConfMongo', 'description': 'mongo配置', 'tree_level': 6},
        {'name': '/ConfRedis', 'description': 'redis配置', 'tree_level': 6},
    ]
    for i in resources_list:
        resources, _ = Resources.objects.get_or_create(name=i['name'], description=i['description'], tree_level=i['tree_level'])
        resources.save()


def init_user_role(user_id, role_id):
    user_role, _ = UserRole.objects.get_or_create(user_id=user_id, role_id=role_id)
    user_role.save()


def init_role_resources(role_id, resource_list):
    for i in resource_list:
        role_resources, _ = RoleResources.objects.get_or_create(role_id=role_id, resources_id=i)
        role_resources.save()


if __name__ == '__main__':
    # init_user()
    # init_role()
    init_resources()
    # 1, 1    2, 5   3, 7
    # init_user_role(3, 7)
    # 1, [1,2,3,4,5,6]    5, [5]   7,[4]
    # init_role_resources(7,[4])
