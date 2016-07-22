from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import ItemForm
from collection.models import Item
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collection.forms import ItemUploadForm
from collection.models import Upload
from collection.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

#def index(request):
#    item = Item.objects.all()
#    return render(request, 'index.html', {'items': item,})



def gallery(request):
    item=Item.objects.all()
    return render(request, 'gallery.html', {'items': item,})


def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    uploads = item.uploads.all()
    return render(request, 'items/item_detail.html', {'item': item, 'uploads': uploads},)

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

@login_required
def edit_item_uploads(request, slug):
    item = Item.objects.get(slug=slug)
    if item.user !=request.user:
        raise Http404
    form_class = ItemUploadForm
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=item)
        if form.is_valid():
            Upload.objects.create(
                image=form.cleaned_data['image'], item=item,
            )
        return redirect('edit_item_uploads', slug=item.slug)
    else:
        form=form_class(instance=item)
    uploads = item.uploads.all()
    return render(request, 'items/edit_item_uploads.html', {
        'item': item,
        'form': form,
        'uploads': uploads,
    })

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
      form = form_class(data=request.POST)

      if form.is_valid():
          contact_name = form.cleaned_data['contact_name']
          contact_email = form.cleaned_data['contact_email']
          form_content = form.cleaned_data['content']

          # Email the profile with the contact info
          template = get_template('contact_template.txt')

          context = Context({
              'contact_name': contact_name,
              'contact_email': contact_email,
              'form_content': form_content,
           })
          content = template.render(context)

          email = EmailMessage(
               'New contact form submission',
               content,
               'Your website <hi@weddinglovely.com>',
               ['youremail@gmail.com'],
               headers = {'Reply-To': contact_email }
           )
          email.send()
          return redirect('contact')
    return render(request, 'contact.html', {'form': form_class,})
