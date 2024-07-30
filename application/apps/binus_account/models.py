from django.db import models


class BinusAccount(models.Model):
    authentication1 = models.TextField()
    authentication2 = models.TextField()

    def __str__(self) -> str:
        return ""
