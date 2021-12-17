import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime




def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    msg = []
    for dirpath, dirnames, filenames in os.walk('.'):
        for dirname in dirnames:
            msg.append(f'Каталог: {os.path.join(dirpath, dirname)}\n')
        for filename in filenames:
            msg.append(f'Файл: {os.path.join(dirpath, filename)}\n')
    return HttpResponse(msg)
    raise NotImplemented

