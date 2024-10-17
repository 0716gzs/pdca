import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
_application = get_wsgi_application()

from apps.auths.models import *
from common import const
from apps.plan.models import PlanLevel


def init_user(plan_level):
    plan_level_list_bulk = []
    for level_dict in plan_level:
        bulk = PlanLevel(name=level_dict['name'], level=level_dict['level'])
        plan_level_list_bulk.append(bulk)
    PlanLevel.objects.bulk_create(plan_level_list_bulk)


if __name__ == '__main__':
    plan_level = [
        {
            'name': '简单',
            'level': const.PlanLevel.EASY,
        },
        {
            'name': '一般',
            'level': const.PlanLevel.NORMAL,
        },
        {
            'name': '困难',
            'level': const.PlanLevel.HARD,
        },
    ]
    init_user(plan_level)
