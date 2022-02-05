from django.db import models
from django.utils import timezone


class ArticleCategory(models.Model):
    """Модель для категории публикаций"""
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'  # эти названия будут показывать в админ панели
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Article(models.Model):
    """Модель для публикации"""
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE,
                                 related_name='articles')  # related_name - для обращения из категории к публикациям
    image = models.ImageField(default='')
    is_new = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['title']

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    """Модель хэштега для публикаций"""
    title = models.CharField(max_length=100, unique=True)
    article = models.ManyToManyField(to=Article)

    class Meta:
        verbose_name = 'Хэштег публикации'
        verbose_name_plural = 'Хэштеги публикаций'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    """Модель комментариев для публикации"""

    article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Коментарии к публикациям'
        verbose_name = 'Коментарий к публикации'

    def __str__(self):
        return self.text
