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

def image_upload(request):
    context = {}
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_up = form.cleaned_data.get("image_up")
            obj = Image.objects.create(image_up = image_up,)
            obj.save()
            print(obj)
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

