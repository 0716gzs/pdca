from django.urls import path
from rest_framework import routers
from apps.auths import views
from apps.auths import login_views, register_view, views

account_urls = [
    # path("GetAuthUrl", login_views.WxLoginView.as_view()),
    # path("wx_qrcode_callback", login_views.WxLoginView.as_view()),
    path("pdca/refresh/token", views.RefreshToken.as_view()),
    path("pdca/captcha", views.CaptchaView.as_view()),
    path("pdca/user/SendCode", views.SendCodeView.as_view()),
    path("pdca/user/register", register_view.RegisterView.as_view()),
    path("pdca/user/login", login_views.LoginView.as_view()),
    path("pdca/user/info", views.UserProfileView.as_view()),
]

account_routers = routers.DefaultRouter(trailing_slash=False)
# account_routers.register(r'system/show_user', login_views.UserViewSet)
