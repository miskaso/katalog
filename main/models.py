from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    category = models.CharField(max_length=55)
    cena = models.IntegerField()
    slug = models.SlugField(null=False, unique='detail')

    def __str__(self):
        return self.name
