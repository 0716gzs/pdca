import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *


def init_resources():
    resources_list = [
        {'name': '/AddUser', 'description': '添加用户'},
        {'name': '/AddRole', 'description': '添加角色'},
        {'name': '/AddResources', 'description': '添加资源url'},
        {'name': '/BugManage', 'description': 'Bug管理'},
        {'name': '/ProjectManage', 'description': '项目管理'},
        {'name': '/Configuration', 'description': '配置管理'},
    ]
    for i in resources_list:
        resources, _ = Resources.objects.get_or_create(name=i['name'], description=i['description'])
        resources.save()


if __name__ == '__main__':
    init_resources()
