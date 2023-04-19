from django.shortcuts import render
from .models import Article

# Create your views here.
def list(request):
  # lay ra tat ca bai viet va sap xep, lay bai viet moi nhat len truoc
  articles = Article.objects.all().order_by("-created_date")
  context = {
    "articles": articles
  }
  return render(request, "articles/articles.html", context)

def detail(request, id):
  article_detail = Article.objects.get(id=id)
  context = {
    "article_detail": article_detail
  }
  return render(request, "articles/detail.html", context)