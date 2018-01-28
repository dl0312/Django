from django.conf.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	re_path(r'^login/$', auth_views.login, name='login', kwargs={
		'template_name': 'accounts/login_form.html',
		}),
	re_path(r'^signup/$', views.signup, name='signup'),
	re_path(r'^profile/$', views.profile, name='profile'),
]