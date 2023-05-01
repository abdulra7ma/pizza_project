from rest_framework.generics import ListAPIView

from pizza.api.serializers import PizzaSerializer
from pizza.models import Pizza


class PizzaAPIView(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
