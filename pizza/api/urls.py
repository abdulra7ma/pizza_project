from django.urls import path
from rest_framework.routers import DefaultRouter

from pizza.api.views import PizzaListAPIView, PizzaCRUDViewSet

router = DefaultRouter()
router.register(r"pizza", PizzaCRUDViewSet)


urlpatterns = [
    path("pizzas/", PizzaListAPIView.as_view(), name="pizzas"),
] + router.urls
