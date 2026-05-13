FROM python:3.11-slim

WORKDIR /app

# Забороняємо Python писати .pyc файли та буферизувати вивід
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копіюємо проєкт
COPY . .

# Збираємо статику і запускаємо Gunicorn
CMD python manage.py collectstatic --noinput && gunicorn car_rental.wsgi:application --bind 0.0.0.0:8000