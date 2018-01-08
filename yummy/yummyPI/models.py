from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.


class Categories(models.Model):
    """Class to create Categories
    """
    category_name = models.CharField(max_length=256)
    category_description = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=int)

    def __str__(self):
        return self.category_name

class Recipes(models.Model):
    """class to create recipes
    """
    recipe_name = models.CharField(max_length=256)
    recipe_ingredients = models.CharField(max_length=256)
    recipe_methods = models.CharField(max_length=256)
    
    def __str__(self):
        return self.recipe_name
    
