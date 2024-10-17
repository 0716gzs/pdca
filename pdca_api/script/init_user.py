import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *


def init_user():
    user, _ = User.objects.get_or_create(username='超级管理员', account='2154195820')
    user.set_password('wowangle')
    user.save()


if __name__ == '__main__':
    init_user()



