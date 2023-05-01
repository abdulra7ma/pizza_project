from django.contrib import admin
from django.urls import path, include

from pizza.views import PizzaListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", PizzaListView.as_view(), name="index"),
]
