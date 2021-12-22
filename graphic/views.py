from django.shortcuts import render
from .forms import ImageForms
# Create your views here.

def graphic(request):
    fm = ImageForms()
    return render(request,'index.html',{'uploadform':fm})

