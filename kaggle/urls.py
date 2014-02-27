from django.conf.urls import patterns, url

from kaggle import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cookie/$', views.cookie, name='cookie'),
    url(r'^form/$', views.form, name='form'),
    url(r'^submit/$', views.submit, name='submit'),
)