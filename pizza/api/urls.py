from django.urls import path

from pizza.api.views import PizzaAPIView

urlpatterns = [
    path("pizza/", PizzaAPIView.as_view(), name="pizza"),
]
