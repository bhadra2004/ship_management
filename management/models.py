from django.db import models

class Ship(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Active")
    image = models.ImageField(upload_to='ships/', null=True, blank=True)

    manufactured_date = models.DateField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='home/', null=True, blank=True)

    def __str__(self):
        return self.title
    


class AboutContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    mission = models.TextField(null=True, blank=True)
    vision = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    

# Create your models here.
