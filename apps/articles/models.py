from django.db import models


class ArticleCategory(models.Model):
    """Модель для категории публикаций"""
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Публикация'  # эти названия будут показывать в админ панели
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Article(models.Model):
    """Модель для публикации"""
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE,
                                 related_name='articles')  # related_name - для обращения из категории к публикациям

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

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
