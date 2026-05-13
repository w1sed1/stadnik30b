import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_msg = data.get('message', '').lower()

            # Логіка відповідей нашого ШІ-асистента
            reply = "Дякую за звернення! Залиште свої контакти, і наш менеджер зв'яжеться з вами найближчим часом."
            
            if any(word in user_msg for word in ["цін", "вартіст", "скільки коштує"]):
                reply = "Ціни на наші авто починаються від 2500 грн/день (наприклад, BMW 3 Series) і сягають 5000 грн/день за преміум-клас (BMW 740i)."
            elif any(word in user_msg for word in ["бронюв", "оренд", "замовити", "взяти"]):
                reply = "Щоб орендувати авто, перейдіть у розділ 'Автопарк', виберіть машину, натисніть 'Перейти до бронювання' та вкажіть бажані дати в календарі."
            elif any(word in user_msg for word in ["привіт", "добрий день", "вітаю"]):
                reply = "Привіт! Я віртуальний асистент DRIVEKNU 🤖. Чим можу допомогти з орендою автомобіля?"
            elif any(word in user_msg for word in ["машин", "авто", "парк"]):
                reply = "В нашому автопарку є автомобілі BMW, Audi, Tesla та Mercedes. Ви можете переглянути їх характеристики на головній сторінці."

            return JsonResponse({'reply': reply})
        except Exception as e:
            return JsonResponse({'reply': 'Вибачте, виникла технічна помилка.'})
            
    return JsonResponse({'error': 'Invalid request'}, status=400)