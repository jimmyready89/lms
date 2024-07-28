from django.db import models


class ScrapingBrowser(models.Model):
    port = models.IntegerField()
    last_login = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return ""


class ScrapingQueue(models.Model):
    comment = models.TextField()
    parameter = models.JSONField()
    response = models.JSONField(default=None, null=True)
    request_datetime = models.DateTimeField(auto_created=True)
    start_datetime = models.DateTimeField(default=None, null=True)
    end_datetime = models.DateTimeField(default=None, null=True)

    def __str__(self) -> str:
        return f"{self.comment} {self.request_datetime}"


class ScrapingActionList(models.Model):
    comment = models.TextField()
    last_used_datetime = models.DateTimeField()
    cooldown_on_minute = models.IntegerField()

    def __str__(self) -> str:
        return ""
