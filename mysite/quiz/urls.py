from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^question/$', views.add_player, name='add_player'),
]
