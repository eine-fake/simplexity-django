from django.conf.urls import url

from . import views

urlpatters = [
	url('r^$', views.index, name='index'),
	url('r^$', views.files, name='files'),
]
