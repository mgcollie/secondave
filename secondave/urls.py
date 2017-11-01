from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, name='login'),
    url(r'^home/$', home),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', auth_views.logout, name='logout'),
    url(r'^logout/$', logout_page),    
]
