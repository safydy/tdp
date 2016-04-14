from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^Detail/(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^Result$', views.ResultsView.as_view(), name='results'),
                       url(r'^test$', views.index, name='index'),
                       )
# urlpatterns = [
#     #ex: /polls/
#     url(r'^$', views.IndexView.as_view(), name='index' ),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView, name='results'),
#     # ex: /polls/5/vote/
#     # url(r'^(?P<question_id>[0-9]+)/vote/$', views.DetailView, name='vote'),
#     url(r'^test', views.index, name='index'),
# ]
