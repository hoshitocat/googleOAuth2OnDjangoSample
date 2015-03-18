from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'google_auth_sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sample_app/$', 'sample_app.views.index'),
    url(r'^sample_app/(?P<sample_app_id>\d+)/$', 'sample_app.views.detail'),
    url(r'^sample_app/(?P<sample_app_id>\d+)/results/$', 'sample_app.views.results'),
    url(r'^sample_app/(?P<sample_app_id>\d+)/vote/$', 'sample_app.views.vote'),

    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
