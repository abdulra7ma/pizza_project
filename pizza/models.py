from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    image = models.ImageField(upload_to="pizza_images")

    def __str__(self):
        return self.name
