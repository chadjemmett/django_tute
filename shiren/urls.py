from django.urls import path
from . import views

app_name = 'shiren'
urlpatterns = [
        path('', views.index, name='index')

        ]
