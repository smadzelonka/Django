from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


# Add new view
def cats_index(req):
    context = {'cats': cats}
    return render(req, 'cats/index.html', context)


# Add the Cat class & list and view function below the imports


class Cat:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]
