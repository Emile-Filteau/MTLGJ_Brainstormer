from django.db import models


class Idea(models.Model):
    name = models.CharField(max_length=256)
    score = models.IntegerField(default=0)


class Activation(models.Model):
    activated = models.BooleanField(default=False)
    showing = models.BooleanField(default=False)