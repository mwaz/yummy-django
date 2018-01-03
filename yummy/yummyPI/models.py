from django.db import models
from django.forms import ModelForm

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=256)
    category_description = models.CharField(max_length=256)

    def __str__(self):
        return self.category_name

class Recipes(models.Model):
    """class to store recipes
    """
    recipe_name = models.CharField(max_length=256)
    recipe_ingredients = models.CharField(max_length=256)
    recipe_methods = models.CharField(max_length=256)
    
    def __str__(self):
        return self.recipe_name
    
