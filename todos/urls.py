from django.urls import path
from . import views


urlpatterns = [
    # Index
    path('', views.index, name= 'index'),

    # Details
    path('details/<int:id>', views.details, name= 'details'),

    # Add
    path('add', views.add, name= 'add'),

    # Edit
    path('edit/<int:id>', views.edit, name= 'edit'),

    # Delete
    path('delete/<int:id>', views.delete, name= 'delete'),

    # Signup
    path('signup', views.signup, name= 'signup'),
]
