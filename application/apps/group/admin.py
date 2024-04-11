from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ['number', 'get_course']
    search_fields = ['course__name']
    list_select_related = ['course']

    @admin.display(ordering='course', description='Course')
    def get_course(self, obj):
        return obj.course.name


admin.site.register(Group, GroupAdmin)
