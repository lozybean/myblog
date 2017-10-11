from datetime import datetime

from article.models import Article, Tag, Category
from django.shortcuts import render, get_object_or_404, get_list_or_404


# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    print(post.id, post.content)
    return render(request, 'post.html', {'post': post})


def archives(request):
    post_list = get_list_or_404(Article)
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def search_tag(request, tag):
    post_list = get_list_or_404(Tag, category_iexact=tag)
    return render(request, 'tag.html', {'post_list': post_list})


def total_tags(request):
    articles = get_list_or_404(Article)
    tag_list = sorted(set([a.category for a in articles]))
    return render(request, 'total_tags.html', {'tag_list': tag_list})


def search_category(request, category):
    post_list = get_list_or_404(Category, category__iexact=category)
    return render(request, 'tag.html', {'post_list': post_list})


def total_category(request):
    articles = get_list_or_404(Category)
    tag_list = sorted(set([a.category for a in articles]))
    return render(request, 'total_tags.html', {'tag_list': tag_list})


def aboutme(request):
    return render(request, 'aboutme.html')


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
