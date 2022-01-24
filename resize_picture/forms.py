from django import forms

class ImageForm(forms.Form):
    image_up = forms.ImageField(label='Your image')
    width = forms.IntegerField(label='width')
    height = forms.IntegerField(label='height',required=False)