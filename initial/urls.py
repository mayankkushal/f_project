from django.urls import path
from . import views

urlpatterns = [
	path('', views.BasicView.as_view(), name='index')
]