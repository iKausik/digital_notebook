from django.db import models
from datetime import datetime
from django.conf import settings

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length= 200)
    text = models.TextField()
    created_at = models.DateTimeField(default= datetime.now, blank= True)


    def __str__(self):
        return self.title
