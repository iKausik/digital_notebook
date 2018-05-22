from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Home page
    path('', include('todos.urls')),

    # Todo
    path('todos/', include('todos.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # User Authetication
    path('accounts/', include('django.contrib.auth.urls')),
]
