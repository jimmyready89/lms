from django.contrib import admin

from .models import People


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'type', 'email']
    search_fields = ['name']


admin.site.register(People, PeopleAdmin)
