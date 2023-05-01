from django.contrib import admin

from pizza.models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    fields = ["name", "description", "price", "image", "size", "amount"]
    search_fields = ["name", "price"]
    list_display = ["name", "description", "price", "size", "amount"]


admin.site.register(Pizza, PizzaAdmin)
