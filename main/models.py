from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from unidecode import unidecode
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    category = models.CharField(max_length=55)
    cena = models.IntegerField()
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True, slugify=lambda value: unidecode(value).replace(' ', '-'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)