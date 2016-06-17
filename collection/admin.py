from django.contrib import admin
#import model
from collection.models import Item
#automated slug creation
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
#register model
admin.site.register(Item, ItemAdmin)
