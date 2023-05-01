
from django.urls import path
from .views import SignUpView, SignInView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("signin", SignInView.as_view(), name="signin"),
    path("signout", LogoutView.as_view(), name="signout"),
]
