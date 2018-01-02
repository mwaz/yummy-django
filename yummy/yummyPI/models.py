from django.db import models
from django.forms import ModelForm

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=256)
    category_description = models.CharField(max_length=256)

    def __str__(self):
        return self.category_name
