from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import foods
from django.utils import timezone
from datetime import timedelta

def index(request):
    total_calories = foods.objects.aggregate(total=Sum('calorie'))['total']
    context = {
        'TotalCal': total_calories
    }
    return render(request, 'index.html', context)

def food(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)

    food_today = foods.objects.filter(date=today)
    food_yesterday = foods.objects.filter(date=yesterday)
    food_older = foods.objects.filter(date__lt=yesterday)
    total_calories = foods.objects.aggregate(total=Sum('calorie'))['total']
    len_foodt = len(food_today)
    len_foody = len(food_yesterday)
    len_foodo = len(food_older)

    context = {
        'Today': food_today,
        'Yesterday': food_yesterday,
        'Older': food_older,
        'LengthT': len_foodt,
        'LengthY': len_foody,
        'LengthO': len_foodo,
        'TotalCal': total_calories
    }

    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST['name']
            calorie = request.POST['calorie']
            
            food_exists = foods.objects.filter(name=name, date=today).exists()

            if not food_exists:
                data = foods(name=name, calorie=calorie)
                data.save()
                print('Food item posted!')
            else:
                print('Item already exists, please update the existing item.')
            return redirect('food')
        elif 'delete' in request.POST:
            id = request.POST.get('delete')
            food = get_object_or_404(foods, id=id)
            food.delete()
            print('Food item deleted!')
            return redirect('food')
        elif 'save' in request.POST:
            id = request.POST.get('save')
            food = get_object_or_404(foods, id=id)
            name = request.POST['edit-name']
            calorie = request.POST['edit-calorie']
            food.name = name
            food.calorie = calorie
            food.save()
            print('Food item updated!')
            return redirect('food')
        elif 'delete-all' in request.POST:
            foods.objects.all().delete()
            print('All food items deleted!')
            return redirect('food')

    return render(request, 'foods.html', context)