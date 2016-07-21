from django.contrib import admin
#import model
from collection.models import Item, Social, Upload
#automated slug creation
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    prepopulated_fields = {'slug': ('name',)}
#register model
admin.site.register(Item, ItemAdmin)

#new admin for Social model
class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('network', 'username',)
#register
admin.site.register(Social, SocialAdmin)

class UploadAdmin(admin.ModelAdmin):
    list_display = ('item',)
    list_display_links = ('item',)
#register
admin.site.register(Upload, UploadAdmin)
