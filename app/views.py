from django.shortcuts import render,get_object_or_404
from datetime import datetime
from .models import Recipe
from .forms import PostForm
from django.shortcuts import redirect



def home(request):
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    return render(request, 'app/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )

def recipes(request):
    reps = Recipe.objects.all()
    return render(request, 'app/recipes.html',
        {
            'title':'My recipes',
            'recipes':reps,
        }
    )

def recipe_info_page(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'app/recipe_info_page.html',
        {
            'title':recipe.recipe_name,
            'image':recipe.recipe_photo.url,
            'desc':recipe.recipe_descr,

        }
    )

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = PostForm()

    return render(request, 'app/recipe_edit.html', {'form': form})
