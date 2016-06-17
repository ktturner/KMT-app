from django.forms import ModelForm
from collection.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description',)
