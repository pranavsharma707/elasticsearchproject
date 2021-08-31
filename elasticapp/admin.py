from django.contrib import admin
from elasticapp.models import Publisher
# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display=['name','address','city','state_province','country','website','latitude','longitude']


admin.site.register(Publisher,PublisherAdmin)


