from django.db import models
from django.contrib.auth.models import User
from cars.models import Car
from datetime import datetime

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if isinstance(self.start_date, str):
            self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, "%Y-%m-%d").date()
        
        days = (self.end_date - self.start_date).days
        if days <= 0:
            self.total_price = self.car.price_per_day
        else:
            self.total_price = days * self.car.price_per_day
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.car.brand} {self.car.model}"