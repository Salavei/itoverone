from django.shortcuts import render
from .forms import ImageForm
from .models import Image


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
            WIDTH = form.cleaned_data.get("width")
            HEIGHT = form.cleaned_data.get("height")
            image_up = form.cleaned_data.get("image_up")
            obj = Image.objects.create(image_up=image_up, )
            ss = str(obj)[-3:-1]
            img = rs_image.open(image_up)
            new_image = img.resize((WIDTH, HEIGHT))
            new_image.save(f'./userpic/{ss + str(image_up)}')
            obj = Image.objects.update(image_up=ss + str(image_up), )
            print('\n' * 10, obj, '\n' * 10)

    else:
        form = ImageForm()
    context['form']= form
    return render(request, "image.html", context)
