from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .forms import NewsForm
from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news,
               'title': 'Список новостей'}
    return render(request,
                  template_name='news/index.html',
                  context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news,
               'category': category}
    return render(request,
                  template_name='news/category.html',
                  context=context)


def view_news(request, news_id):
    # item = News.objects.get(pk=news_id)
    item = get_object_or_404(News, pk = news_id)
    return render(request, 'news/view_news.html', {'item': item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})