from django.http import Http404
from django.views import generic

from apps.articles.models import Article


class ArticleListView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'article-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list'] = Article.objects.all()
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
        return context
