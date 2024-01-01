from django.urls import path
from rest_framework import routers
from apps.auths import views
from apps.auths import login_views

account_urls = [
    path("api/v1/user/login", login_views.LoginView.as_view()),
    path("api/v1/user/register", login_views.RegisterView.as_view()),
    path("api/v1/user/info", views.UserProfileView.as_view()),
]

account_routers = routers.DefaultRouter(trailing_slash=False)
# account_routers.register(r'system/show_user', login_views.UserViewSet)
