from django.db import models


class Idea(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
