from article import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test/$', views.test, name='test'),
    url(r'^post/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutme/$', views.aboutme, name='about_me'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.search_tag, name='search_tag'),
    url(r'^category/(?P<category_id>\d+)/$', views.search_category, name='search_category'),
    url(r'^total_tags/$', views.total_tags, name='total_tags'),
    url(r'^total_category/$', views.total_category, name='total_category'),
    url(r'^search/$', views.search_blog, name='search_blog'),
]
