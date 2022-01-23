from django.contrib import admin
from .models import Article, ArticleCategory, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass
