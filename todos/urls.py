# Importing path just like we do in project/urls.py
from django.urls import path
# Here . means current folder
from . import views

# Routes for different pages in the todo app
urlpatterns = [
    # Route/url for index page
    path('', views.index, name= 'index'),

    # Route for Details/single todo detail page
    path('details/<int:id>', views.details, name= 'details'),

    # Rote for Add new todo form
    path('add', views.add, name= 'add'),

    # Route for Edit form
    path('edit/<int:id>', views.edit, name= 'edit'),

    # Route for Delete todo
    path('delete/<int:id>', views.delete, name= 'delete'),

    # Route for Signup page
    path('signup', views.signup, name= 'signup'),
]
