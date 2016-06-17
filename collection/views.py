from django.shortcuts import render, redirect
from collection.forms import ItemForm
from collection.models import Item

def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items': item,})

def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'items/item_detail.html', {'item': item},)

def edit_item(request, slug):
    item = Item.objects.get(slug=slug)
    form_class = ItemForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance = item)
        if form.is_valid:
            form.save()
            return redirect('item_detail', slug=item.slug)
    else:
        form = form_class(instance = item)
    return render(request, 'items/edit_item.html', {'item': item, 'form': form,})
