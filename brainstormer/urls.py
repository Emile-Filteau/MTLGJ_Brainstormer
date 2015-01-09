from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from brainstormer import views, settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_idea', views.add_idea, name='add_idea'),
    url(r'^like/(?P<idea_id>\d+)', views.like, name='like'),
    url(r'^add_to_favorites/(?P<idea_id>\d+)', views.add_to_favorites, name='add_to_favorites'),
    url(r'^favorites/', views.my_favorites, name='favorites'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
