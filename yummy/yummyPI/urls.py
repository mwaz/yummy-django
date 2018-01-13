from django.conf.urls import url
from . views import home, create_category, view_created_categories, create_recipe, view_recipes
from django.contrib.auth import views as auth_views
from . import views

app_name = 'yummy_recipes'
urlpatterns = [
    url(r'^$', view_created_categories, name='home'),
    url(r'^Register/$', views.register),
    url(r'^Category$', create_category,   name='category'),
    url(r'^Recipe/$', create_recipe,   name='recipe'),
    url(r'^Category/<category_id>/RecipeView/$', view_recipes,   name='recipe'),
    url(r'^Login/$', auth_views.login,  {'template_name': 'login.html'}, name='login'),
    url(r'^Logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout')
]
