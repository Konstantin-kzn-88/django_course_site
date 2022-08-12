from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .forms import NewsForm
from .models import News, Category


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html' # собственный шаблон
    context_object_name = 'news' # собственный объект итерирования для рендеринга
    extra_context = {'title': 'Главная'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
    # Собственные запрос  только опубликованных новаостей
    def get_queryset(self):
        return  News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False # запретить показ отсутствующих категорий

    def get_queryset(self):
        return  News.objects.filter(category_id = self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {'news': news,
#                'title': 'Список новостей'}
#     return render(request,
#                   template_name='news/index.html',
#                   context=context)


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
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})