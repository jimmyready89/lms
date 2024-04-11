from django.contrib import admin
from .models import Quiz, Assignment


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'take_date', 'status', 'duration', 'score']
    search_fields = ['title']


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'sent_date', 'status', 'score']
    search_fields = ['title']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Assignment, AssignmentAdmin)
