from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

menu = [{'title': "О сайте", 'url_name':'about'},
        {'title': "Подобрать компьютер", 'url_name':'test'},]


def about(request):
    return render(request, 'compapp/about.html', {'menu': menu, 'title': 'О сайте'})


def test_page(request):
    return render(request, 'compapp/index.html', {'menu': menu, 'title': 'Подобрать компьютер'})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')