from django.views.generic import ListView, TemplateView

from pizza.models import Pizza


class MainView(TemplateView):
    template_name = "index.html"


class MenuView(ListView):
    template_name = "order.html"
    context_object_name = "pizzas"
    queryset = Pizza.objects.all()

