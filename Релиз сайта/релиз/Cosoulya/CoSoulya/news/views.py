from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def news_home(request):
    news = Article.objects.order_by("-date")
    return render(request, "news/news_home.html", {"news": news})

def create(request):
    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма неверна"

    form = ArticleForm()

    data = {
        "form": form,
        "error": error
    }
    return render(request, "news/create.html", data)
