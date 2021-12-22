from django import forms
from django.db.models import fields
from .models import PhotoModel
class ImageForms(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = "__all__"
        labels = {'photos':''}