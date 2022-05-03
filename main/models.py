from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todolist', null=True)
    title = models.CharField(max_length=225)

    def _str_(self):
        return self.title


class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    content = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content
