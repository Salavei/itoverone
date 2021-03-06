from django.test import TestCase
from .models import Image


class ImageTestCase(TestCase):
    def setUp(self):
        Image.objects.create(image_up="image22.png")
        Image.objects.create(image_up="image12.png")

    def test_image(self):
        image22 = Image.objects.get(image_up="image22.png")
        image12 = Image.objects.get(image_up="image12.png")
        self.assertEqual(image22, image22)
        self.assertEqual(image12, image12)