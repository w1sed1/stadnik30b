from celery import shared_task
import openai
from django.conf import settings
from cars.models import Car

@shared_task
def generate_car_description(car_id):
    try:
        car = Car.objects.get(id=car_id)
        openai.api_key = settings.OPENAI_API_KEY
        
        prompt = f"Згенеруй привабливий рекламний опис українською мовою для сервісу оренди автомобілів. Автомобіль: {car.brand} {car.model} {car.year} року."
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        
        description = response.choices[0].message.content.strip()
        car.description = description
        car.save()
        return f"Успішно згенеровано для авто {car_id}"
    except Exception as e:
        return str(e)