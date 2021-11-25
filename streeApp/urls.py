from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.createPost, name='createPost'),
    path('update/', views.updatePost, name='updatePost'),
    path('update/<int:edit_id>', views.edit, name='edit'),

]










