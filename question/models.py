from django.db import models

# Create your models here.
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    answer = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse('category', kwargs={'type_id': self.pk})

    def __str__(self):
        return self.title