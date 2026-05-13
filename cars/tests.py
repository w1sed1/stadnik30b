from django.test import TestCase
from .models import Car

class CarModelTest(TestCase):
    def setUp(self):
        Car.objects.create(
            brand="BMW",
            model="X5",
            year=2023,
            price_per_day=3000.00
        )

    def test_car_creation(self):
        car = Car.objects.get(brand="BMW")
        self.assertEqual(car.model, "X5")
        self.assertEqual(car.year, 2023)