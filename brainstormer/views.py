from django.shortcuts import render, redirect
from brainstormer import models, forms
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    ideas = models.Idea.objects.order_by('-score')
    return render(request, 'index.html', {'ideas': ideas})


def add_idea(request):
    form = forms.AddIdeaForm(request.POST)
    if form.is_valid():
        idea = models.Idea.objects.create(name=form.cleaned_data['name'])
        idea.save()
    return redirect('index')


def vote_up(request, idea_id):
    try:
        idea = models.Idea.objects.get(pk=idea_id)
        idea.score += 1
        idea.save()
    except ObjectDoesNotExists:
        pass
    return redirect('index')


def vote_down(request, idea_id):
    try:
        idea = models.Idea.objects.get(pk=idea_id)
        idea.score -= 1
        idea.save()
    except ObjectDoesNotExists:
        pass
    return redirect('index')
