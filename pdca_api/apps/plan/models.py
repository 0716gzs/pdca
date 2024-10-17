import datetime

from django.contrib.auth.hashers import (
    check_password, make_password
)
from django.db import models
from django.db.models import PositiveSmallIntegerField

from common import const
from common.fields import FileIdField
from common.fields import SimpleForeignKey
from common.models import BaseModel


class Plan(BaseModel):
    name = models.CharField(max_length=64, default='', null=True, blank=True, help_text='计划名称')
    start_time = models.DateTimeField(default=datetime.datetime.now, help_text='开始时间')
    end_time = models.DateTimeField(default=datetime.datetime.now, help_text='结束时间')
    level = PositiveSmallIntegerField(choices=const.PlanLevel.CHOICES,
                                      default=const.PlanLevel.EASY,
                                      help_text='等级')
    user = SimpleForeignKey('auths.User', related_name='plan_user')

    class Meta:
        db_table = 'plan'
        verbose_name = verbose_name_plural = '计划困难等级表'
