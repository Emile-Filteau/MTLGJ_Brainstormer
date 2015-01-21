from django.shortcuts import render, redirect
from brainstormer import models, forms
from django.core.exceptions import ObjectDoesNotExist


def index(request, notice=None):
    activation = models.Activation.objects.first()
    if activation.activated:
        likes = []
        if request.session.get('like_list'):
            likes = request.session.get('like_list').split(',')
        else:
            request.session['like_list'] = ''

        favorites = []
        if request.session.get('fav_list'):
            favorites = request.session.get('fav_list').split(',')
        else:
            request.session['fav_list'] = ''

        ideas = models.Idea.objects.order_by('-score')
    else:
        likes = []
        favorites = []
        ideas = []
    return render(request, 'index.html', {'ideas': ideas, 'likes': likes, 'favorites': favorites, 'activation': activation})


def add_idea(request):
    activation = models.Activation.objects.first()
    if activation.activated:
        form = forms.AddIdeaForm(request.POST)
        if form.is_valid():
            idea = models.Idea.objects.create(name=form.cleaned_data['name'])
            idea.save()
    return redirect('index')


def like(request, idea_id):
    activation = models.Activation.objects.first()
    if activation.activated and activation.showing:
        if request.session.get('like_list'):
            likes = request.session.get('like_list').split(',')
        else:
            likes = []

        try:
            idea = models.Idea.objects.get(pk=idea_id)
            if not idea_id in likes:
                idea.score += 1
                likes.append(idea_id)
            else:
                idea.score -= 1
                likes.remove(idea_id)
            request.session['like_list'] = ",".join(likes)
            idea.save()

        except ObjectDoesNotExist:
            pass

    return redirect('index')


def add_to_favorites(request, idea_id):
    activation = models.Activation.objects.first()
    if activation.activated and activation.showing:
        if request.session.get('fav_list'):
            favs = request.session.get('fav_list').split(',')
        else:
            favs = []

        try:
            if not idea_id in favs:
                favs.append(idea_id)
            else:
                favs.remove(idea_id)
            request.session['fav_list'] = ",".join(favs)
        except ObjectDoesNotExist:
            pass
    return redirect('index')


def remove_from_favorites(request, idea_id):
    activation = models.Activation.objects.first()
    if activation.activated and activation.showing:
        add_to_favorites(request, idea_id)
    return redirect('favorites')


def my_favorites(request):
    activation = models.Activation.objects.first()
    if activation.activated and activation.showing:
        favorites = []
        if request.session.get('fav_list'):
            favorites = request.session.get('fav_list').split(',')

        ideas = []
        for favorite in favorites:
            try:
                ideas.append(models.Idea.objects.get(pk=int(favorite)))
            except ObjectDoesNotExist:
                pass

        return render(request, 'favorites.html', {'ideas': ideas})
    else:
        return redirect('index')