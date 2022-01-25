from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from .func_im import resize
from django.http import HttpResponseRedirect

from PIL import Image as rs_image
import hashlib


def resize_img(request):
    link = Image.objects.order_by('-id')[0]
    result = hashlib.md5(str(link).encode())
    im = rs_image.open(f'./userpic/{str(link)}')
    (width, height) = im.size
    link_text = f'{result.hexdigest()}_{width}_x_{height}.{str(link)[-3:]}'
    return render(request, 'link.html', {'link': link, 'link_text':link_text})


def image_upload(request):
    context = {}
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get("height") is None:
                WIDTH = form.cleaned_data.get("width")
                HEIGHT = WIDTH
                image_up = form.cleaned_data.get("image_up")
                resize(image_up, WIDTH, HEIGHT)
                return HttpResponseRedirect('resize_img/')
            else:
                WIDTH = form.cleaned_data.get("width")
                HEIGHT = form.cleaned_data.get("height")
                image_up = form.cleaned_data.get("image_up")
                resize(image_up, WIDTH, HEIGHT)
                return HttpResponseRedirect('resize_img/')
    else:
        form = ImageForm()
    context['form']= form
    return render(request, "image.html", context)
