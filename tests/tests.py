import shutil
import unittest
import os
from PIL import Image
from main import resize_by_width, increase_height, BASE_DIR


class TestResizePhotoForMarketplace(unittest.TestCase):
    def test_resize_photo(self):
        """
        Test if the size of resized image is equal to needed.
        In this test the sample image width-1200.jpg with width 1200 is taken.
        Then the copy width-1200-copy.jpg is made. Then resize copy and check of the width of the copy
        is equal to needed (800 in our case). Then delete copy.
        """
        root = BASE_DIR / 'tests/img'
        shutil.copyfile(root / 'width-1200.jpg', root / 'width-1200-copy.jpg')
        path = root / 'width-1200-copy.jpg'
        with Image.open(path) as image:
            resize_by_width(image, 800)
        with Image.open(path) as image:
            self.assertEqual(image.width, 800)
        os.remove(path)

    def test_increase_height(self):
        """
        Test the increase of height. Take sample. Copy it, increase height and check
        if it is equal to needed height.
        :return:
        """
        root = BASE_DIR / 'tests/img'
        shutil.copyfile(root / 'height-576.jpg', root / 'height-576-copy.jpg')
        path = root / 'height-576-copy.jpg'
        with Image.open(path) as image:
            increase_height(image, 800)
        with Image.open(path) as image:
            self.assertEqual(image.height, 800)
        os.remove(path)
