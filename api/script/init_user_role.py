import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *


def init_user_role():
    pass


if __name__ == '__main__':
    init_user_role()
