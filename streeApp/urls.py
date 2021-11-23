from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.createPost, name='createPost'),
    path('update/', views.updatePost, name='updatePost'),

    # path('<slug:post>/', views.post_single, name='post_single'),

]










