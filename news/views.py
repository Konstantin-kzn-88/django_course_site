from django.shortcuts import render

from .models import News

def index(request):
    news = News.objects.order_by('-created_at')
    return render(request,
                  template_name='news/index.html',
                  context={'news': news,'title': 'Список новостей'})
