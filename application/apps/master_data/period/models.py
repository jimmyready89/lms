from django.db import models


class Period(models.Model):
    description = models.CharField(max_length=300)
    url = models.URLField()

    def __str__(self) -> str:
        return self.description
