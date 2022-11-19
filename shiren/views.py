from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item, Price
from django.urls import reverse
from django.views import generic
from .forms import ItemForm

# Create your views here.

def index(request):
    form = ItemForm()
    return render(request, "shiren/index.html",{'form': form } )


def list(request):
    value  = request.POST.get('price')
    price = get_object_or_404(Price, item_price=value)
    items = Item.objects.filter(price_id=price.id)
    print(items)



    print(Price)
    # items = Price.objects.get(item_price=price)
    # print(items)




    context ={}
    return render(request, "shiren/list_items.html", context)
