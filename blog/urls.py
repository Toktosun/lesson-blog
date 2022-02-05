"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from apps.articles.views import ArticleListView, ArticleDetailView, BlogView, \
    BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', ArticleListView.as_view()),  # Показ всех публикаций
    path('articles/<int:pk>/', ArticleDetailView.as_view(),
         name='article-detail-url'),  # Получать детальную страницу публикации
    path('blog/', BlogView.as_view()),
    path('blog/<int:category_pk>/', BlogDetailView.as_view(), name='blog-detail'),
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
