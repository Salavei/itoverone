from django.urls import path

from .views import image_upload, resize_img

urlpatterns = [
    path('',image_upload, name='home'),
    path('resize_img/',resize_img)
]
