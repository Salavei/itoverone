# from django.shortcuts import render
# from django.views.generic import ListView
#
# from .models import Image
# # Create your views here.
#
# class ImageView(ListView):
#     model = Image

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .models import Image

import copy

from PIL import Image as rs_image

import random
def image_upload(request):
    context = {}
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_up = form.cleaned_data.get("image_up")
            # obj = Image.objects.create(image_up = image_up,)
            # aaaa = str(random.randint(100, 500)) + str(image_up)

            obj = Image.objects.create(image_up=image_up, )
            image_path = f'./userpic/{obj}'
            ss = str(obj)[-3:-1]
            img = rs_image.open(image_up)
            # # получаем ширину и высоту
            new_image = img.resize((400, 400))
            new_image.save(f'./userpic/{ss + str(image_up)}')

            obj = Image.objects.update(image_up=ss + str(image_up), )

            print('\n' * 10 ,ss ,obj, '\n' * 10)
    else:
        form = ImageForm()


    context['form']= form
    return render(request, "image.html", context)

# def image_upload(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST)
#         print(form)
#         if form.is_valid():
#             Image(image_up=form).save()
#             return HttpResponseRedirect('')
#     else:
#         form = ImageForm()
#
#     return render(request, 'image.html', {'form': form}, print(form))

