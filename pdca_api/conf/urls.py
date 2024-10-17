"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from apps.auths.urls import account_urls, account_routers
from apps.plan.urls import plan_urls, plan_routers

urlpatterns = [
    # api
    # BaseModelViewSet 路由
    path('pdca/admin/', admin.site.urls),
    path('pdca/', include(account_routers.urls)),
    path('pdca/', include(plan_routers.urls)),
]
# 不基于modelviewset的路由
# ======= 业务 Api Views =============
urlpatterns += account_urls
urlpatterns += plan_urls
