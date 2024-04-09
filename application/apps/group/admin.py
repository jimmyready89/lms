from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ['number']
    search_fields = ['number']


admin.site.register(Group, GroupAdmin)
