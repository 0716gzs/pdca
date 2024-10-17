import datetime
from django.db import models
from django.db.models import PositiveSmallIntegerField
from common import const
from common.fields import SimpleForeignKey
from common.models import BaseModel


class Project(BaseModel):
    number = models.CharField(max_length=16, default='', help_text='项目标识号')
    pro_logo = SimpleForeignKey('upload.FileInfo', related_name='project_person_in_charge', help_text='项目logo')
    name = models.CharField(max_length=64, default='', null=True, blank=True, help_text='项目名称')
    description = models.CharField(max_length=255, default='', null=True, blank=True, help_text='描述')
    type = PositiveSmallIntegerField(choices=const.ProjectType.CHOICES,
                                     default=const.ProjectType.INTERIOR,
                                     help_text='项目类型')
    status = PositiveSmallIntegerField(choices=const.ProjectStatus.CHOICES,
                                       default=const.ProjectStatus.NOT_YET_STARTED,
                                       help_text='项目状态')
    start_time = models.DateTimeField(default=datetime.datetime.now, help_text='开始时间')
    end_time = models.DateTimeField(default=datetime.datetime.now, help_text='结束时间')
    person_in_charge = SimpleForeignKey('auths.User', related_name='project_person_in_charge', help_text='负责人')


class ProjectTeam(BaseModel):
    """
        那个组负责的这个项目
    """
    pass
