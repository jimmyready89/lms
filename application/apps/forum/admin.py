from django.contrib import admin
from .models import ForumSession, ForumThread, ForumComment


class ForumSessionAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'start_date', 'end_date', 'get_course']
    search_fields = ['number', 'title']
    list_select_related = ['course']

    @admin.display(ordering='course', description='Course')
    def get_course(self, obj):
        return obj.course.name


class ForumThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'get_people', 'get_session']
    search_fields = ['title', 'get_people', 'get_session']
    list_select_related = ['people', 'session']

    @admin.display(ordering='people', description='People')
    def get_people(self, obj):
        return obj.people.name

    @admin.display(ordering='session', description='Session')
    def get_session(self, obj):
        return obj.session.title


class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'created', 'get_people', 'get_thread']
    search_fields = ['get_people', 'get_thread']
    list_select_related = ['people', 'thread']

    @admin.display(ordering='people', description='People')
    def get_people(self, obj):
        return obj.people.name

    @admin.display(ordering='thread', description='Thread')
    def get_thread(self, obj):
        return obj.thread.title


admin.site.register(ForumSession, ForumSessionAdmin)
admin.site.register(ForumThread, ForumThreadAdmin)
admin.site.register(ForumComment, ForumCommentAdmin)
