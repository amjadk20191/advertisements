from django.contrib import admin

from .models import complaints, connect_with_us, opinion  


@admin.register(complaints)
class complaintsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'email', 'phone')


@admin.register(connect_with_us)
class connect_with_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'email', 'phone')


@admin.register(opinion)
class opinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'active')
    list_filter = ('active',)