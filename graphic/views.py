from django.shortcuts import render

from graphic.models import PhotoModel
from .forms import ImageForms
# Create your views here.

def graphic(request):
    img = PhotoModel.objects.all()
    return render(request,'index.html',{'img':img})

