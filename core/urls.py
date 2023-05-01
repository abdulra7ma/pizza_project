from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pizza.views import MainView, MenuView, PricingView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", MainView.as_view(), name="index"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("pricing/", PricingView.as_view(), name="pricing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
