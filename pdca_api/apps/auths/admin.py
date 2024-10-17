from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
# 注册模型类
admin.site.register([User])
