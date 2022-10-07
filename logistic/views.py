import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from config.settings import TG_BOT_TOKEN, TG_GROUP_ID
from .forms import MyUserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url='home')


def registration_modal(request):
    user = User.objects.create_user(username=request.GET['username'], tg_username=request.GET['tg_username'], password=request.GET['password1'])
    login(request, user)
    return redirect('home')


def auth_modal(request):
    if request.user.is_authenticated:
        return redirect('home')

    username = request.GET.get('username').lower()
    password = request.GET.get('password1')
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse('no_user')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('correct')
    else:
        return HttpResponse('incorrect')


def logout_user(request):
    logout(request)
    return redirect('home')


def home_page(request):
    social_links = SocialLinks.objects.get(id=1)
    order_statistics = OrderStatistics.objects.get(id=1)
    reviews = Reviews.objects.all()
    order_configs = OrdersConfig.objects.all()
    order_config = OrdersConfig.objects.get(pk=1)
    context = {
        'social_links': social_links,
        'order_statistics': order_statistics,
        'reviews': reviews,
        'order_configs': order_configs,
        'order_config': order_config,
    }
    return render(request, 'home.html', context=context)


def get_and_send_ti_admin(request):
    user = User.objects.get(username=request.user.username)
    country = request.GET.get('country')
    country_index = request.GET.get('country_index')
    price = request.GET.get('price')
    order_width = request.GET.get('order_width')
    city = request.GET.get('city')
    order_weight = request.GET.get('order_weight')
    order_weight_opt = request.GET.get('order_weight_opt')
    order_lenght = request.GET.get('order_lenght')
    order_height = request.GET.get('order_height')
    context = f"Username: {user.username}\n" \
              f"TG-AKK: {'ADMIN' if len(user.tg_username) == 0 else '@' + user.tg_username}\n\n" \
              f"Страна: {country}\n" \
              f"Индекс: {country_index}\n" \
              f"Стоимость товара, $: {price}\n" \
              f"Ширина, см: {order_width}\n" \
              f"Город: {city}\n" \
              f"Вес посылки: {order_weight}{order_weight_opt}\n" \
              f"Длина, см: {order_lenght}\n" \
              f"Высота, см: {order_height}\n"
    requests.post(f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={TG_GROUP_ID}&text={context}')

    return HttpResponse('True')


def get_order_data(request):
    ocd = OrdersConfig.objects.get(pk=request.GET.get('pk')).__dict__
    data = {
        'title': ocd['title'],
        'logistic_days': ocd['logistic_days'],
        'price': ocd['price'],
        'description': ocd['description'],
        'max_weight': ocd['max_weight'],
        'volume_weight': ocd['volume_weight'],
        'max_size': ocd['max_size'],
        'traking_link': ocd['traking_link'],
        'departure_frequency': ocd['departure_frequency'],
        'exception': ocd['exception'],
        }
    return JsonResponse(data, safe=False)

