from django.shortcuts import render, redirect
# from django.http import HttpResponse
import uuid
import boto3
from .models import Cat, Toy, Photo
from .forms import Cat_Form, Feeding_Form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# the line below add @login_required
from django.contrib.auth.decorators import login_required


# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollection'

# Create your views here.


def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


# Add new view
@login_required
def cats_index(req):
    # create
    if req.method == 'POST':
        cat_form = Cat_Form(req.POST)
        if cat_form.is_valid():
            new_cat = cat_form.save(commit=False)
            new_cat.user = req.user
            new_cat.save()
            return redirect('index')

    # Retrieve list of cats, filtered by the
    # logged-in user stored on the request object
    cats = Cat.objects.filter(user=req.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    cat_form = Cat_Form()
    context = {'cats': cats, 'cat_form': cat_form}
    return render(req, 'cats/index.html', context)


@login_required
def cats_detail(req, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = Feeding_Form()
    toys_cat_doesnt_have = Toy.objects.exclude(
        id__in=cat.toys.all().values_list('id'))
    context = {'cat': cat, 'feeding_form': feeding_form,
               'available_toys': toys_cat_doesnt_have}
    return render(req, 'cats/detail.html', context)


@login_required
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


@login_required
def cats_delete(req, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect('index')
# =================== Feeding routes =========================


@login_required
def add_feeding(req, cat_id):
    # create the ModelForm using the data in request.POST
    form = Feeding_Form(req.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cats_detail', cat_id=cat_id)

# =================== toy routes =========================


@login_required
def assoc_toy(req, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cats_detail', cat_id=cat_id)


@login_required
def deassoc_toy(req, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('cats_detail', cat_id=cat_id)

# =================== Photo routes =========================


@login_required
def add_photo(request, cat_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('cats_detail', cat_id=cat_id)

# =================== Auth routes =========================


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or a bad POST request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


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
