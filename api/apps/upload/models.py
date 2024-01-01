from django.db import models

from common import const
from common.models import BaseModel


class FileInfo(BaseModel):
    full_filename = models.CharField(max_length=255, help_text='文件全名')
    filename = models.CharField(max_length=255, help_text='文件名')
    extension = models.CharField(max_length=16, help_text='文件后缀')
    md5 = models.CharField(max_length=64, help_text='文件md5值')
    path = models.CharField(max_length=512, help_text='文件相对路径')
    size = models.BigIntegerField()

    class Meta:
        db_table = 'file_info'
        verbose_name = verbose_name_plural = '文件信息'
