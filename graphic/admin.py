from django.contrib import admin
from .models import PhotoModel
# Register your models here.

# @admin.register(PhotoModel)
# class PhotoModelAdmin(admin.ModelAdmin):
#     list_display= ['image']

@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['id','image_tag','video']


    def image_tag(self,obj):
        return obj.image_tag

    image_tag.allow_tag= True
