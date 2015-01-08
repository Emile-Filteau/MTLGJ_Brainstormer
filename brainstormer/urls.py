from django.conf.urls import patterns, include, url
from django.contrib import admin
from brainstormer import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brainstormer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^add_idea', views.add_idea, name='add_idea'),
    url(r'^vote_up/(?P<idea_id>\d+)', views.vote_up, name='vote_up'),
    url(r'^vote_down/(?P<idea_id>\d+)', views.vote_down, name='vote_down'),
    url(r'^admin/', include(admin.site.urls)),
)
