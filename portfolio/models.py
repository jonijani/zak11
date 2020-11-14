from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/images')

# Create your models here.
