from django.db import models
from django.utils.translation import gettext_lazy as _


class AssessmentStatus(models.IntegerChoices):
    OPEN = 1, _('Open')
    COMPLETED = 2, _('Completed')
    EXPIRED = 3, _('Expired')


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    take_date = models.DateTimeField(null=True)
    status = models.PositiveSmallIntegerField(choices=AssessmentStatus.choices, default=AssessmentStatus.OPEN)
    duration = models.IntegerField(help_text='Save in minutes')
    score = models.IntegerField(null=True)
    course = models.ForeignKey('courses.Courses', related_name='quizes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    sent_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=AssessmentStatus.choices, default=AssessmentStatus.OPEN)
    student_comment = models.TextField(blank=True, null=True)
    instructor_comment = models.TextField(blank=True, null=True)
    score = models.IntegerField(null=True)
    course = models.ForeignKey('courses.Courses', related_name='assignments', on_delete=models.CASCADE)
    instructor = models.ForeignKey('people.People', related_name='assignment_comments', on_delete=models.CASCADE)
    last_sender = models.ForeignKey('people.People', related_name='last_sender_assignments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
