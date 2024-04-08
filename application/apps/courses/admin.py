from django.contrib import admin

from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'type', 'subject', 'period']
    search_fields = ['code', 'name']


admin.site.register(Courses, CoursesAdmin)
