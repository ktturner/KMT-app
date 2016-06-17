
from django.conf.urls import patterns, url
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
    url(r'^admin/', admin.site.urls),
]
