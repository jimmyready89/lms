from django.db import models


class Group(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey('courses.Courses', related_name='groups', on_delete=models.CASCADE)
    peoples = models.ManyToManyField('people.People', related_name='groups')

    def __str__(self) -> str:
        return f"Group {self.number} in ({self.course.name})"
