from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comp.views.home', name='home'),
	url(r'^kaggle/', include('kaggle.urls', namespace="kaggle")),
    url(r'^admin/', include(admin.site.urls)),
)
