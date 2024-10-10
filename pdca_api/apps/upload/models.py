from datetime import datetime

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
    file_type = models.PositiveSmallIntegerField(choices=const.FileType.CHOICES,
                                                 default=const.FileType.UPLOAD,
                                                 help_text='文件类型')

    class Meta:
        db_table = 'file_info'
        verbose_name = verbose_name_plural = '文件信息'


class DataStudentScore(BaseModel):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    edu_commission_id = models.BigIntegerField()
    grade_type = models.CharField(max_length=10, blank=True, null=True)
    school_id = models.BigIntegerField()
    base_grade_id = models.BigIntegerField()
    grade_id = models.BigIntegerField()
    class_id = models.BigIntegerField()
    student_ID = models.CharField(max_length=20, blank=True, null=True)
    plan_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    projectNumber = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    grade_name = models.CharField(max_length=20, blank=True, null=True)
    class_name = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    device_number = models.CharField(max_length=200, blank=True, null=True)
    achievement = models.CharField(max_length=20, blank=True, null=True)
    achievement_int = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    score = models.DecimalField(max_digits=20, decimal_places=0)
    score_grade = models.CharField(max_length=20, blank=True, null=True)
    score_weight = models.DecimalField(max_digits=20, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=1)
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    remark = models.CharField(max_length=999, blank=True, null=True)
    create_at = models.DateTimeField(default=datetime.now)

    class Meta:
        managed = False
        db_table = 'data_student_score'

        # 联合索引
        # index_together = ["edu_commission_id", "grade_type", "plan_id", "project_id"]
