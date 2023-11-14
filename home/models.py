from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateField()
    post = models.TextField()
