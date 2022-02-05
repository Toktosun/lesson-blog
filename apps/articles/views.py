import random

from django.http import Http404
from django.views import generic

from apps.articles.models import Article, ArticleComment, ArticleCategory


class ArticleListView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'article-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list'] = Article.objects.all()
        context['random_hello'] = random.choice(["Hi", "Hello", "Салам"])
        return context


class ArticleDetailView(generic.TemplateView):
    """Представление для получения детальной страницы публикации"""
    template_name = 'article-detail.html'

    def get_context_data(self, **kwargs):
        context = dict()
        article_pk = kwargs['pk']  # primary key который хочет получит клиент
        try:
            context['article'] = Article.objects.get(id=article_pk)
        except Article.DoesNotExist:
            raise Http404
        context['article_comments'] = ArticleComment.objects.all()
        return context


class BlogView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['category_list'] = ArticleCategory.objects.all()
        context['article_list'] = Article.objects.all()
        return context


class BlogDetailView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        category_pk = kwargs['category_pk']
        context['category_list'] = ArticleCategory.objects.all()
        # первый способ
        context['article_list'] = Article.objects.filter(category_id=category_pk)
        # альтернативный способ
        # cat = ArticleCategory.objects.get(id=category_pk)
        # context['article_list'] = Article.objects.filter(category=cat)
        return context
