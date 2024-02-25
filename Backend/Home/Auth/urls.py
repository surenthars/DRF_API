from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("users", views.GetUsers.as_view(), name="users"),
    path("jwt/create", TokenObtainPairView.as_view(), name="jwt_create_view"),
    path("jwt/refresh", TokenRefreshView.as_view(), name="jwt_refresh_view"),
    path("jwt/verify", TokenVerifyView.as_view(), name="jwt_verify_view"),
]
