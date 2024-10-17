import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *


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


if __name__ == '__main__':
    init_role()
