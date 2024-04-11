from django.db import models


class ForumSession(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    course = models.ForeignKey('courses.Courses', related_name='sessions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number


class ForumThread(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    people = models.ForeignKey('people.People', related_name='created_threads', on_delete=models.CASCADE)
    session = models.ForeignKey(ForumSession, related_name='threads', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class ForumComment(models.Model):
    body = models.TextField()
    created = models.DateTimeField()
    people = models.ForeignKey('people.People', related_name='comments', on_delete=models.CASCADE)
    thread = models.ForeignKey(ForumThread, related_name='comments', on_delete=models.CASCADE)
    comment = models.ForeignKey('forum.ForumComment', related_name='replies', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body
