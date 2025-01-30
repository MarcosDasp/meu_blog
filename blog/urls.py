from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('criar_post/', views.criar_post, name='criar_post'),
]
