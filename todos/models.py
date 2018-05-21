from django.db import models
# This is a python DateTime module
from datetime import datetime
# This for accessing current logged in user current user
from django.conf import settings

class Todo(models.Model):
    # This is making a foreignkey from the current logged in user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length= 200)
    text = models.TextField()
    created_at = models.DateTimeField(default= datetime.now, blank= True)   # Here I'm using python DateTime for showing current date and time

    # This is for displaying the proper title string, not as object
    def __str__(self):
        return self.title
