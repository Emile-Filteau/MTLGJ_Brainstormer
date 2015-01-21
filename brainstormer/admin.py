from django.contrib import admin
from brainstormer import models


@admin.register(models.Idea)
class IdeaAdmin(admin.ModelAdmin):
    fields = ['name', 'score']
    list_display = ['name', 'score']

@admin.register(models.Activation)
class ActivationAdmin(admin.ModelAdmin):
    fields = ['activated', 'showing']
    list_display = ['activated', 'showing']