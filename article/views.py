import os
from datetime import datetime

from article.models import Article, Category, Tag
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse


# Create your views here.
class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-created_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created_time

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('detail:post_id', {'post_id': item.id})


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
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


def search_blog(request):
    if 'key' in request.GET:
        key = request.GET['key']
        if not key:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=key)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


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
    md_file = os.path.join(settings.BASE_DIR, 'static', 'md', 'about_me.md')
    with open(md_file, encoding='utf-8') as fp:
        md_data = fp.read()
    return render(request, 'aboutme.html', {'md': md_data})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
