from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('date')
    context = {
        'news': news
    }
    return render(request, 'news/news_home.html', context)

def create(request):
    return render(request, 'news/create.html')


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_namee = 'article' #объект который передается в шаблон