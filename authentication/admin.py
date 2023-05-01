from django.contrib import admin

from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ["email", "name"]
    list_display = ["email", "name"]
    search_fields = ["email", "name"]


admin.site.register(User, UserAdmin)
