from django.views.generic import ListView

from pizza.models import Pizza


class PizzaListView(ListView):
    template_name = "index.html"
    context_object_name = "pizzas"
    queryset = Pizza.objects.all()
    paginate_by = 4
