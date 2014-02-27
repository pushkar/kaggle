from django.conf.urls import patterns, url

from kaggle import views

urlpatterns = patterns('',
    url(r'^leaderboard/(?P<order_by>\w*)$', views.leaderboard, name='leaderboard'),
    url(r'^cookie/$', views.cookie, name='cookie'),
    url(r'^form/$', views.form, name='form'),
    url(r'^submit/$', views.submit, name='submit'),
)