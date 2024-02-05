from django.shortcuts import render


def index(request):
    context = {'topic': 'Главная страница'}
    return render(request, 'mainapp/index.html', context)

def about(request):
    return render(request, 'mainapp/about.html')


