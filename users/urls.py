from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path("accounts/password_change/", views.LoginUser.as_view()),
    path("accounts/registration/", views.RegisterNewUser.as_view(), name='user_registration'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.Register.as_view(), name="register")
]
