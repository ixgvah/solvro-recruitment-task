from django.db import models

# Create your models here.

class Cocktail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cocktails/', blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
