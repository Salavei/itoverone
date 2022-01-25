# from PIL import Image as rs_image
# from .models import Image
#
# def resize(image_up, WIDTH,HEIGHT, *args, **kwargs):
#     obj = Image.objects.create(image_up=image_up, )
#     ss = str(obj)[-3:-1]
#     img = rs_image.open(image_up)
#     new_image = img.resize((WIDTH, HEIGHT))
#     new_image.save(f'./userpic/{ss + str(image_up)}')
#     give_photo = Image.objects.update(image_up=ss + str(image_up), )
#
#     wefew = Image.objects.filter(image_up=f"Image object{give_photo}")
#     return print(wefew)