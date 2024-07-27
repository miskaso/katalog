from django.db import models
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    category = models.CharField(max_length=55)
    cena = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

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