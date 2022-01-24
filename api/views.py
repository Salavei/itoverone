from rest_framework import generics
from resize_picture.models import Image
from .serializers import ImageSerializer




# Create your views here.
class ImageApiView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



class ImageDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer