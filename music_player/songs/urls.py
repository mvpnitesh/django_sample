from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^songs/', views.get_songs),
	url(r'^$', views.get_homepage)
]