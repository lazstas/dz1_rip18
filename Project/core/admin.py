from django.contrib import admin
from .models import Computer, Order


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
