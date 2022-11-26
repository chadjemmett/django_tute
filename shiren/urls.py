from django.urls import path
from . import views

app_name = 'shiren'
urlpatterns = [
        path('', views.index, name='index'),
        path('list', views.list, name='list'),
        path('check', views.check, name='check')

        ]
