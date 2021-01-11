from django.urls import path
from . import views
# single dot means current directory or root


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>', views.cats_detail, name='cats_detail'),
    path('cats/<int:cat_id>/edit/', views.cats_edit, name='cats_edit'),
    path('cats/<int:cat_id>/delete/', views.cats_delete, name='cats_delete'),
]
