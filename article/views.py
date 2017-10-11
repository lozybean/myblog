from datetime import datetime

from article.models import Article, Category, Tag
from django.shortcuts import render, get_object_or_404, get_list_or_404


# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    post.count_read += 1
    post.save()
    return render(request, 'post.html', {'post': post})


def archives(request):
    post_list = get_list_or_404(Article)
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def search_tag(request, tag_id):
    print(tag_id)
    post_list = get_list_or_404(Article, tags__id=int(tag_id))
    return render(request, 'tag.html', {'post_list': post_list})


def total_tags(request):
    tag_list = get_list_or_404(Tag)
    return render(request, 'total_tags.html', {'tag_list': tag_list})


def search_category(request, category_id):
    post_list = get_list_or_404(Article, category__id=int(category_id))
    return render(request, 'category.html', {'post_list': post_list})


def total_category(request):
    category_list = get_list_or_404(Category)
    return render(request, 'total_category.html', {'category_list': category_list})


def aboutme(request):
    return render(request, 'aboutme.html')


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
