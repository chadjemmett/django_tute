from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item
from django.urls import reverse
from django.views import generic
from .forms import ItemForm, ListForm

# Create your views herte.

def index(request):
    form = ItemForm()
    found_items = Item.objects.filter(found=True)
    return render(request, "shiren/index.html",{'form': form, 'data': found_items, 'thing': "hello world" } )


def list(request):
    value  = request.POST.get('price')
    transaction = request.POST.get('transaction')
    item_type = request.POST.get('item_type')
    if transaction == 'buy':
        items = Item.objects.filter(item_type=item_type).filter(buy_price=value)
    if transaction == 'sell':
        items = Item.objects.filter(item_type=item_type).filter(sell_price=value)
    form = ListForm()

    context ={'items': items, "form": form}
    return render(request, "shiren/list_items.html", context)


def check(request):
    items = request.POST.getlist('item_id')
    for i in items:
        thing =Item.objects.get(pk=i)
        thing.found = True
        thing.save()

    form = ItemForm()
    found_items = Item.objects.filter(found=True)

    context = {'form': form, 'data': found_items}
    return redirect('index', kwargs={"form": form} )

def reset(request):
    Item.objects.all().update(found=False)

    form = ItemForm()
    return redirect("/shiren")
