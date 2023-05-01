from django.contrib import admin
from django.urls import path, include

from pizza.views import MainView, MenuView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", MainView.as_view(), name="index"),
    path("menu/", MenuView.as_view(), name="menu"),
]
