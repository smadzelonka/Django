from django.urls import path
from . import views
# single dot means current directory or root


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
]
