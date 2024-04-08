from django.db import models
from ..period.models import Period
from django.utils.translation import gettext_lazy as _


class Courses(models.Model):
    class TypeChoices(models.IntegerChoices):
        CL = (1, _('CL'))
        LEC = (2, _('LEC'))

    subject = models.CharField(max_length=300, db_column="subject_code")
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    type = models.IntegerField(choices=TypeChoices)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, db_column="period_id")
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
