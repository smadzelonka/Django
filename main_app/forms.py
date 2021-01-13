from django.forms import ModelForm
from .models import Cat, Feeding


class Cat_Form(ModelForm):
    class Meta:
        model = Cat
        labels = {'name': 'Cat Name'}
        fields = ['name', 'breed', 'description', 'age']


class Feeding_Form(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
