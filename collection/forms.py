from django.forms import ModelForm
from collection.models import Item
from collection.models import Upload

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description',)

class ItemUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('image',)
