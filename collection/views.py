from django.shortcuts import render
from collection.models import Item

def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items': item,})
