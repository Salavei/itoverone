from .models import Image

import time
from PIL import Image as rs_image


def resize(image_up, WIDTH,HEIGHT, *args, **kwargs):
    new_name = str(time.time()) + str(image_up)
    Image.objects.create(image_up=new_name)
    img = rs_image.open(image_up)
    new_image = img.resize((WIDTH, HEIGHT))
    new_image.save(f'./userpic/{new_name}')
    Image.objects.filter(image_up=new_name).update(image_up=new_name)
