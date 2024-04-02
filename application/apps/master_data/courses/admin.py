from django.contrib import admin

from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['type', 'period', 'subject']
    search_fields = ['description']


admin.site.register(Courses, CoursesAdmin)
