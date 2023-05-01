from django.views.generic import ListView, TemplateView

from pizza.models import Pizza
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(TemplateView):
    template_name = "index.html"


class MenuView(LoginRequiredMixin, ListView):
    template_name = "order.html"
    context_object_name = "pizzas"
    queryset = Pizza.objects.all()


class PricingView(LoginRequiredMixin, ListView):
    template_name = "pricing.html"
    context_object_name = "pizzas"
    queryset = Pizza.objects.all()
