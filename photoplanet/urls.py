from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'photoplanet.views.home', name='home'),
    url(
        r'^all/',
        TemplateView.as_view(template_name="photoplanet/all.html"),
        name='all'),
    url(
        r'^about/',
        TemplateView.as_view(template_name="photoplanet/about.html"),
        name='about'),
    url(
        r'^day/',
        TemplateView.as_view(template_name="photoplanet/day.html"),
        name='day'),
    url(r'', include('users.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
)