// Зачекати, поки HTML-документ повністю завантажиться
document.addEventListener('DOMContentLoaded', function() {
    // Знайти контейнер календаря
    var calendarEl = document.getElementById('calendar');
    
    // Перевірити, чи існує контейнер на цій сторінці
    if (calendarEl) {
        // Створити екземпляр календаря
        var calendar = new FullCalendar.Calendar(calendarEl, {
            // Вибрати початковий вигляд (наприклад, місяць)
            initialView: 'dayGridMonth',
            
            // Налаштувати заголовок (навігація)
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            
            // Вибрати українську локалізацію (за бажанням)
            locale: 'uk', 
            
            // === ГОЛОВНЕ НАЛАШТУВАННЯ: ДЖЕРЕЛО ПОДІЙ ===
            // Ми вказуємо шлях до нашого JSON API
            events: '/api/bookings/', 
            
            // За бажанням: що робити при кліку на подію (бронювання)
            eventClick: function(info) {
                alert('Бронювання: ' + info.event.title + '\nПеріод: ' + info.event.start.toLocaleDateString() + ' - ' + info.event.end.toLocaleDateString());
            }
        });
        
        // Відмалювати календар
        calendar.render();
    }
});