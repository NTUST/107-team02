from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index , name='index'),
	url(r'^$', views.post_detail1 , name='post_detail1'),
	url(r'^$', views.post_area , name='post_area'),
	url(r'^$', views.post_about , name='post_about'),
	url(r'^$', views.post_museum , name='post_museum'),
	url(r'^$', views.post_m_type , name='post_m_type'),
	url(r'^$', views.comment , name='comment'),
]