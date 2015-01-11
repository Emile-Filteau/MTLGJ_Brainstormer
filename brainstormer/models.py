from django.db import models


class Idea(models.Model):
    name = models.TextField()
    score = models.IntegerField(default=0)
