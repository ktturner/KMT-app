from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import ItemForm
from collection.models import Item
from django.contrib.auth.decorators import login_required
from django.http import Http404
#from collection.forms import ItemUploadForm
#from collection.models import Upload

def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items': item,})



def gallery(request):
    item=Item.objects.all()
    return render(request, 'gallery.html', {'items': item,})


def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    #grab object's social media accounts
    social_accounts = item.social_accounts.all()
    #uploads = item.uploads.all()
    return render(request, 'items/item_detail.html', {'item': item, 'social_accounts': social_accounts,})#'uploads': uploads})


@login_required
def edit_item(request, slug):
    item = Item.objects.get(slug=slug)
    if item.user != request.user:
        raise Http404
    form_class = ItemForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', slug=item.slug)
    else:
        form = form_class(instance = item)
    return render(request, 'items/edit_item.html', {'item': item, 'form': form,})

def create_item(request):
    form_class = ItemForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.slug = slugify(item.name)
            return redirect('item_detail', slug = item.slug)
    else:
        form =form_class()
    return render(request, 'items/create_item.html', {'form': form, })

def browse_by_name (request, initial=None):
    if initial:
        items = Item.objects.filter(name__istartswith=initial).order_by('name')
    else:
        items = Item.objects.all().order_by('name')
    return render(request, 'search/search.html', {'items': items, 'initial': initial,})

#@login_required
#def edit_item_uploads(request, slug):
#    item=Item.objects.get(slug=slug)
#    if item.user != request.user:
#        raise Http404
#    form_class = ItemUploadForm
#    if request.method == 'POST':
##        if form.is_valid():
##            return redirect('edit_item_uploads', slug=item.slug)
##    uploads=item.uploads.all()
#    return render(request, 'items/edit_item_uploads.html', {'item':item, 'form':form, 'uploads':uploads,})
