from django.conf.urls import url
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'), # post list
	re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # content of the post
	re_path(r'^post/new/$', views.post_new, name='post_new'), # new post
	re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # edit post
	re_path(r'^post/(?P<pk>\d+)/comments/new/$', views.comment_new, name='comment_new'), # new comment
	re_path(r'^post/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'), # edit comment
	re_path(r'^post/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'), # delete comment
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)