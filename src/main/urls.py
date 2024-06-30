from django.urls import path
from .views import index, article_detail, add_article

urlpatterns = [
    path('', index, name='main-index'),
    path('article/<int:article_id>/', article_detail, name='article.content'),
    path('add_article/', add_article, name='new_article'),
]
