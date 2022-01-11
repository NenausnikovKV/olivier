from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Dish, DishComponent


def index(request):
    return HttpResponse("Hello")


def dishes(request):
    dish_list = Dish.objects.order_by("name").exclude(name="Отсутствует")
    context = {'dish_list': dish_list}
    return render(request, 'ol/dishes.html', context)

def dish_components(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    dish_component_list = dish.dishcomponent_set.exclude(name="Отсутствует")
    context = {'dish_component_list': dish_component_list, "dish_name": dish.name}
    return render(request, 'ol/dish_components.html', context)

