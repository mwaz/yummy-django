from django.conf.urls import url
from . views import home, create_category
from django.contrib.auth import views as auth_views
from . import views

app_name = 'yummy_recipes'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^Register/$', views.register),
    url(r'^Category/$', create_category,   name='category'),
    url(r'^Login/$', auth_views.login,  {'template_name': 'login.html'}, name='login'),
    url(r'^Logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout')
]