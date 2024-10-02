import datetime

from django.http import Http404
from django.shortcuts import render

from django.http import HttpResponse


from main.models import Car


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    context = {'cars': cars}
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(pk=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'car': car})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(pk=car_id)
        sales = car.sale_set.all()
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
