from django.contrib import admin
# Importing Todo model
# Here . means current folder
from .models import Todo

# Registering the model to display on the Admin panel
admin.site.register(Todo)
