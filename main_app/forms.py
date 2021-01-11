from django.forms import ModelForm
from .models import Cat


class Cat_Form(ModelForm):
    class Meta:
        model = Cat
        labels = {'name': 'Cat Name'}
        fields = ['name', 'breed', 'description', 'age']
