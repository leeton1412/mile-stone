from django.db import models


class Category(models.Model):
    """ Creating Categories model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Creating Products model """
    category = models.ForeignKey('Category', null=True, blank=True, 
    on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    ingredients = models.CharField(max_length=600)
    allergens = models.CharField(max_length=600)
    is_vegan = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
