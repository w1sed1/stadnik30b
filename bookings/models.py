from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.start_date and self.end_date and self.car:
            days = (self.end_date - self.start_date).days
            if days > 0:
                self.total_price = days * self.car.price_per_day
            else:
                self.total_price = self.car.price_per_day
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.car} ({self.start_date} to {self.end_date})"