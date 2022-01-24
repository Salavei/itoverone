from django.shortcuts import render
from .forms import ImageForm


def image_upload_view(request):
    return render(request, 'index.html', {'form': ImageForm})