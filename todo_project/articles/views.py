from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url='accounts:login')
def article_homepage(request):
    if request.method == 'GET':
        articles = models.Article.objects.all().order_by('-date')
        article_count = models.Article.objects.all().count()
        return render(request, 'articles/articles_index.html', {'articles': articles, 'count':article_count,'active2':'active'})


@login_required(login_url='accounts:login')
def article_owned(request):
    if request.method == 'GET':
        articles = models.Article.objects.all().filter(author=request.user.id).order_by('-date')
        article_count = models.Article.objects.all().filter(author=request.user.id).count()
        return render(request, 'articles/articles_my_article.html', {'articles': articles, 'count':article_count, 'active3':'active'})


@login_required(login_url='accounts:login')
def article_detail(request, id=0):
    article = models.Article.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'articles/articles_detail.html', {'article':article })


@login_required(login_url='accounts:login')
def article_detail_own(request, id=0):
    article = models.Article.objects.get(id=id)
    if request.method == 'GET':
        if request.user == article.author:
            return render(request, 'articles/articles_detail_owner.html', {'article':article, 'active3':'active'})
        else:
            return HttpResponse('Bad Request')



@login_required(login_url='accounts:login')
def article_create(request, id=0):
    if id==0:        
        if request.method == 'GET':
            form = forms.CreateArticle()
            return render(request, 'articles/articles_create.html', {'forms': form, 'active1':'active', 'btnName':'Create'})
        elif request.method == 'POST':
            form = forms.CreateArticle(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('articles:list')
    elif id > 0:
        article = models.Article.objects.get(id=id)
        if request.method == 'GET':
            form = forms.CreateArticle(instance=article)
            return render(request, 'articles/articles_create.html', {'forms': form, 'active1':'active', 'btnName':'Update'})
        elif request.method == 'POST':
            form = forms.CreateArticle(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:owned')



@login_required(login_url='accounts:login')
def article_delete(request, id):
    try:
        article = models.Article.objects.get(id=id)
        art_count = models.Article.objects.all().filter(id=id).count()
        if request.method == 'POST':
            article.delete()
            return redirect('articles:owned')
    except Exception as e:
        return redirect('articles:owned')
