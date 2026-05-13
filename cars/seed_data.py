import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental.settings')
django.setup()

from cars.models import Car

cars_data = [
    {
        "brand": "BMW", "model": "3 Series (G20)", "year": 2019, "price_per_day": 2500.00, 
        "engine": "2.0L B47 Diesel", "transmission": "Автомат", "fuel_type": "Дизель", 
        "mileage": 65000, "seats": 5, "description": "Потужний дизельний двигун B47, клімат-контроль та комфортний салон."
    },
    {
        "brand": "Audi", "model": "A4", "year": 2021, "price_per_day": 2800.00, 
        "engine": "2.0L TFSI", "transmission": "Автомат", "fuel_type": "Бензин", 
        "mileage": 42000, "seats": 5, "description": "Сучасний седан з передовими технологіями."
    },
    {
        "brand": "Tesla", "model": "Model 3", "year": 2022, "price_per_day": 3500.00, 
        "engine": "Dual Motor", "transmission": "Редуктор", "fuel_type": "Електро", 
        "mileage": 25000, "seats": 5, "description": "Електричний комфорт та неймовірна динаміка."
    },
    {
        "brand": "Mercedes-Benz", "model": "C43 AMG", "year": 2021, "price_per_day": 4500.00, 
        "engine": "3.0L V6 BiTurbo", "transmission": "Автомат", "fuel_type": "Бензин", 
        "mileage": 35000, "seats": 5, "description": "Спортивний седан із потужним двигуном."
    },
    {
        "brand": "BMW", "model": "740i", "year": 2019, "price_per_day": 5000.00, 
        "engine": "3.0L I6 Turbo", "transmission": "Автомат", "fuel_type": "Бензин", 
        "mileage": 52000, "seats": 5, "description": "Представницький седан класу люкс."
    },
    {
        "brand": "Audi", "model": "S6", "year": 2021, "price_per_day": 4800.00, 
        "engine": "2.9L V6 TFSI", "transmission": "Автомат", "fuel_type": "Бензин", 
        "mileage": 28000, "seats": 5, "description": "Динамічний седан з системою повного приводу."
    }
]

# ОЧИЩАЄМО БАЗУ ВІД СТАРИХ АВТО
Car.objects.all().delete()

# ДОДАЄМО НОВІ АВТО З УСІМА ДАНИМИ
for item in cars_data:
    Car.objects.create(**item)

print("Базу успішно оновлено!")