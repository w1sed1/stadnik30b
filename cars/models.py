from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    engine = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"