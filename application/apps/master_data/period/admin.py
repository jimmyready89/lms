from django.contrib import admin

from .models import Period


class PeriodAdmin(admin.ModelAdmin):
    list_display = ['description', 'url']
    search_fields = ['description']


admin.site.register(Period, PeriodAdmin)
