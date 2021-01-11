from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Cat
from .forms import Cat_Form

# Create your views here.


def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


# Add new view
def cats_index(req):
    # create
    if req.method == 'POST':
        cat_form = Cat_Form(req.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('index')

    cats = Cat.objects.all()
    cat_form = Cat_Form()
    context = {'cats': cats, 'cat_form': cat_form}
    return render(req, 'cats/index.html', context)


def cats_detail(req, cat_id):
    cat = Cat.objects.get(id=cat_id)
    context = {'cat': cat}
    return render(req, 'cats/detail.html', context)


def cats_edit(req, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if req.method == 'POST':
        cat_form = Cat_Form(req.POST, instance=cat)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('cats_detail', cat_id=cat.id)

    cat_form = Cat_Form(instance=cat)
    context = {'cat_form': cat_form, 'cat': cat}
    return render(req, 'cats/edit.html', context)


def cats_delete(req, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect('index')


# Add the Cat class & list and view function below the imports
# class Cat:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]
