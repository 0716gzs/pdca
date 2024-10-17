from django.urls import path
from rest_framework import routers
from apps.plan import views

plan_urls = [
    # path("pdca/plan/level", views.PlanLevelViewSet.as_view()),
]

plan_routers = routers.DefaultRouter(trailing_slash=False)
plan_routers.register(r'plan', views.PlanViewSet)
