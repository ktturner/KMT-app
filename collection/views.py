from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import ItemForm
from collection.models import Item
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items': item,})

def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'items/item_detail.html', {'item': item},)

@login_required
def edit_item(request, slug):
    item = Item.objects.get(slug=slug)
    if item.user != request.user:
        raise Http404
    form_class = ItemForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance = item)
        if form.is_valid:
            form.save()
            return redirect('item_detail', slug=item.slug)
    else:
        form = form_class(instance = item)
    return render(request, 'items/edit_item.html', {'item': item, 'form': form,})

def create_item(request):
    form_class = ThingForm
    if request.method == 'POST'
        form = form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.slug = slugify(item.name)
            item.save()
            return redirect('item_detail', slug = item.slug)
        else:
            form = form_class()
        return render(request, 'items/create_item.html', {'form': form,})
