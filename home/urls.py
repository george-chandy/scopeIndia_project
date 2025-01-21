from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # You can change this to your actual view
]
