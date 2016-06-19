from django.contrib.auth.views import (password_reset, password_reset_done,
     password_reset_confirm, password_reset_complete)
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^content/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^items/(?P<slug>[-\w]+)/$', views.item_detail, name='item_detail'),
    url(r'^items/(?P<slug>[-\w]+)/edit/$', views.edit_item, name='edit_item'),

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

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),

]
