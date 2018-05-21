"""todolist_project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Importing include

# Here we connect all apps available in this project
# We're not adding pages from those apps, only the root url of the app is added
urlpatterns = [
    # This is for Home page
    # Making Todos app as the home page
    path('', include('todos.urls')),

    # This is for Todos App, this is also the home page, added above.
    path('todos/', include('todos.urls')),

    # This is for Admin page
    path('admin/', admin.site.urls),

    # This url is for login, logout and password management
    path('accounts/', include('django.contrib.auth.urls')),
]
