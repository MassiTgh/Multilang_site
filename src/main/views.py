from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from main.models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )
    else:
        articles = Article.objects.all()
    return render(request, "main/index.html", {'article_list': articles, 'query': query})  # Affiche tous les articles par défaut ou champs de recherche vide

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "main/content.html", {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirection vers la liste des articles après l'ajout
    else:
        form = ArticleForm()
    return render(request, "main/add_article.html", {'form': form})
