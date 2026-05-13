from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from cars.models import Car
import calendar as pycalendar

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def book_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        overlapping = Booking.objects.filter(
            car=car,
            start_date__lte=end_date,
            end_date__gte=start_date
        ).exists()

        if overlapping:
            messages.error(request, 'Автомобіль вже заброньовано на ці дати.')
        else:
            Booking.objects.create(
                user=request.user,
                car=car,
                start_date=start_date,
                end_date=end_date
            )
            messages.success(request, 'Бронювання успішне!')
            return redirect('calendar')

    return render(request, 'bookings/book_car.html', {'car': car})

def calendar(request):
    today = timezone.now().date()
    cal = pycalendar.Calendar(firstweekday=0)
    month_days = cal.monthdatescalendar(today.year, today.month)
    
    calendar_data = []
    for week in month_days:
        week_data = []
        for day in week:
            bookings = Booking.objects.filter(start_date__lte=day, end_date__gte=day).select_related('car')
            booked_cars = [f"{b.car.brand} {b.car.model}" for b in bookings]
            
            week_data.append({
                'date': day,
                'day': day.day,
                'is_current_month': day.month == today.month,
                'booked_cars': booked_cars,
                'is_past': day < today
            })
        calendar_data.append(week_data)

    return render(request, 'bookings/calendar.html', {
        'calendar_data': calendar_data,
        'today': today
    })