from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from random import sample

def main(request):
    recipes = list(Recipe.objects.all())
    random_recipes = sample(recipes, min(10, len(recipes)))
    return render(request, 'main.html', {'recipes': random_recipes})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.all()
    return render(request, 'category_detail.html', {'category': category, 'recipes': recipes})
