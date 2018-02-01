from django.conf.urls import re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
	re_path(r'^login/$', auth_views.login, name='login',
		kwargs={'template_name': 'accounts/login_form.html',}
	),
	re_path(r'^signup/$', views.signup, name='signup'),
	re_path(r'^profile/$', views.profile, name='profile'),
	re_path(r'^logout/$', auth_views.logout, name='logout',
		kwargs={'next_page': 'post_list',}
	)
]