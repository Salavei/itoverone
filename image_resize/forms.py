from django import forms
from resize_picture.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'