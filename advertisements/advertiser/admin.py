from django.contrib import admin

from .models import advertisement, seen_advertisement


@admin.register(advertisement)
class advertisementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'name',
        'country',
        'description',
        'URL',
        'image',
        'cative',
    )
    list_filter = ('user', 'cative')
    search_fields = ('name',)


@admin.register(seen_advertisement)
class seen_advertisementAdmin(admin.ModelAdmin):     
    list_display = ('id', 'user', 'advertisement')   
    list_filter = ('user', 'advertisement')