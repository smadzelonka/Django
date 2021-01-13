from django.urls import path
from . import views
# single dot means current directory or root


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>', views.cats_detail, name='cats_detail'),
    path('cats/<int:cat_id>/edit/', views.cats_edit, name='cats_edit'),
    path('cats/<int:cat_id>/delete/', views.cats_delete, name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    # amazon photos s3
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
    # associate a toy with a cat (M:M)
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
    path('cats/<int:cat_id>/deassoc_toy/<int:toy_id>/',
         views.deassoc_toy, name='deassoc_toy'),

]
