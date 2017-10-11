from article import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test/$', views.test, name='test'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutme/$', views.aboutme, name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^total_tags/$', views.total_tags, name='total_tags'),
]
