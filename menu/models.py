from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/%Y/%m/%d/", default="nophoto.jpg")
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
