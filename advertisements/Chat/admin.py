from django.contrib import admin

from .models import chat


@admin.register(chat)
class chatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_chat', 'system_chat')
    list_filter = ('user',)