from collection.backends import MyRegistrationView
from django.contrib.auth.views import (password_reset, password_reset_done,
     password_reset_confirm, password_reset_complete)
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from collection import views
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    #url(r'^contact/$',
    #    TemplateView.as_view(template_name='contact.html'),
    #    name='contact'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^gallery/$', views.gallery, name='gallery'),

    url(r'^items/$', RedirectView.as_view(pattern_name='browse', permanent=True)),

    url(r'^items/(?P<slug>[-\w]+)/$', views.item_detail, name='item_detail'),
    url(r'^items/(?P<slug>[-\w]+)/edit/$', views.edit_item, name='edit_item'),

    url(r'^items/(?P<slug>[-\w]+)/edit/images/$', views.edit_item_uploads, name='edit_item_uploads'),

    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=True)),

    url(r'^browse/name/$', views.browse_by_name, name='browse'),

    url(r'^browse/name/(?P<initial>[-\w]+)/$', views.browse_by_name, name='browse_by_name'),

    url(r'^accounts/password/reset/$', password_reset, {'template_name':
        'registration/password_reset_form.html'}, name="password_reset"),

    url(r'^accounts/password/reset/done/$', password_reset_done,
       {'template_name':'registration/password_reset_done.html'},
       name = "password_reset_done"),

    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name = "password_reset_confirm"),

    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name = "password_reset_complete"),

    url(r'^accounts/register/$', MyRegistrationView.as_view(), name = 'registration_register'),

    url(r'^accounts/create_item/$', views.create_item, name='registration_create_item'),


    url(r'^accounts/', include('registration.backends.simple.urls')),


    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),]
