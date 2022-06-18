from django.db import models


class UserPost(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=2000)
