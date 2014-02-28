from django.conf.urls import patterns, url

from kaggle import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^pages/(?P<page_id>\w+)$', views.page_view, name='page_view'),
    url(r'^leaderboard/(?P<order_by>\w*)$', views.leaderboard, name='leaderboard'),
    url(r'^set_cookie/$', views.set_cookie, name='set_cookie'),
    url(r'^show_cookie/$', views.show_cookie, name='show_cookie'),
    url(r'^form/$', views.form, name='form'),
    url(r'^submit/$', views.submit, name='submit'),
)