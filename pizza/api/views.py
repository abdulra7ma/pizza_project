from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from pizza.api.serializers import PizzaSerializer
from pizza.models import Pizza


class PizzaListAPIView(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaCRUDViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer