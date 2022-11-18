from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item
from django.urls import reverse
from django.views import generic

class ItemView(generic.ListView):
    template_name="shiren/index.html"

    def get_queryset(self):
        return Item.objects.all()

# Create your views here.



