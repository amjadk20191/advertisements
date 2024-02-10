from django.contrib import admin

from .models import plan


@admin.register(plan)
class planAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_of_day', 'price')
    search_fields = ('name',)