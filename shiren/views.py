from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item
from django.urls import reverse
from django.views import generic
from .forms import ItemForm

# Create your views here.

def index(request):
    form = ItemForm(request.POST)
    print(vars(request))
    return render(request, "shiren/index.html", {'form': form})


def item_list(request):
    pass
