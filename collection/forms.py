from django.forms import ModelForm
from collection.models import Item
from collection.models import Upload
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description',)

class ItemUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('image',)

class ContactForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
