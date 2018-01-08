from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .models import Categories, Recipes
from .forms import UserRegistrationForm, CategoryRegistrationForm, RecipeRegistrationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/yummyPI/')
            else:
                raise forms.ValidationError('Looks like a user with that username or email exists')
    else:
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})

    # def login(request):
    #     return HttpResponseRedirect('/yummyPI/')


@login_required
def create_category(request):
    """Method to create a new category
    """
    if request.method == 'POST':
        form = CategoryRegistrationForm(request.POST)
        
        created_by = request.user.id
        if form.is_valid():
            
            catObj = form.cleaned_data
            category_name = catObj['category_name']
            category_description = catObj['category_description']
            if not (Categories.objects.filter(category_name=category_name).exists()):
                Categories.objects.create(category_name=category_name, category_description=category_description, created_by_id=created_by)


               
                return HttpResponseRedirect('/yummyPI/')
            else:
                raise forms.ValidationError('Looks like such a category exists')
    else:
        form = CategoryRegistrationForm()
    return render(request, 'categories.html', {'form': form})

def view_created_categories(request):
    """Method to view categories
    """
    category_object = Categories.objects.all()
    return render(request, 'home.html', {'category_object': category_object})

def create_recipe(request):
    """Method to create a recipe from a category
    """
    form = RecipeRegistrationForm(request.POST)
    if form.is_valid():
        recipe_obj = form.cleaned_data
        recipe_name = recipe_obj['recipe_name']
        recipe_methods = recipe_obj['recipe_methods']
        recipe_ingredients = recipe_obj['recipe_ingredients']
    
        existing_recipe = Recipes.objects.filter(recipe_name=recipe_name).exists()
        if not existing_recipe:
            Recipes.objects.create(recipe_name=recipe_name, recipe_methods=recipe_methods, recipe_ingredients=recipe_ingredients)
            return HttpResponseRedirect('/yummyPI/RecipeView')
        else:
            raise forms.ValidationError('I am sorry looks like the recipe name exists')
    else:
        form = RecipeRegistrationForm()
    return render(request, 'recipes.html', {'form': form})

def view_recipes(request):
    """Method to fetch created recipes
    """
    recipe_object = Recipes.objects.all()
    return render(request, 'recipeView.html', {'recipe_object': recipe_object})





