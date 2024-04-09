from django.db import models


class Group(models.Model):
    number = models.IntegerField()
    peoples = models.ManyToManyField('people.People', related_name='groups')

    def __str__(self) -> str:
        return f"Group {self.number}"
