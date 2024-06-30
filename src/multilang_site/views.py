from django.shortcuts import render

def index(request):
    return render(request, "multilang_site/index.html")