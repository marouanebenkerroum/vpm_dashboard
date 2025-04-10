from django.urls import path
from . import views

#Redirect to index function in views.py
urlpatterns = [
 path('', views.index, name='index'),

]