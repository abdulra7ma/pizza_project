from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(
        max_length=255,
        choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")],
    )
    amount = models.IntegerField(default=1)
    image = models.ImageField(upload_to="pizza_images")

    def __str__(self):
        return self.name
