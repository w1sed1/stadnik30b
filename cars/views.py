from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car
from bookings.models import Booking

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def book_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        conflicts = Booking.objects.filter(
            car=car,
            start_date__lte=end_date,
            end_date__gte=start_date
        )
        
        if not conflicts.exists():
            Booking.objects.create(
                user=request.user,
                car=car,
                start_date=start_date,
                end_date=end_date
            )
            return redirect('car_list')
        else:
            return render(request, 'cars/book_car.html', {'car': car, 'error': 'Автомобіль недоступний на ці дати.'})
            
    return render(request, 'cars/book_car.html', {'car': car})