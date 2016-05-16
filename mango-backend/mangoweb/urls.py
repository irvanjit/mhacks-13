from django.conf.urls import patterns, include, url
from django.contrib import admin
import pdb
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^usertoken/', 'mangoapp.views.add_user'),
    url(r'^list/', 'mangoapp.views.update_or_return_list'),
)
