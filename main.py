from pathlib import Path
from PIL import Image, UnidentifiedImageError
import os
import shutil


BASE_DIR = Path(__file__).resolve().parent


def resize_by_width(image, new_width):
    """
    Resize image to new width
    :param new_width: new width of image
    :param image: PIL image
    """
    coefficient = new_width / image.width
    new_height = int(image.height * coefficient)
    image_resized = image.resize((new_width, new_height))
    image_resized.save(image.filename)


def increase_height(image, new_height):
    """
    Increase height of image
    :param image: PIL image
    :param new_height: needed image height
    """
    if image.height >= new_height:
        return False
    width, height = image.size
    result = Image.new(image.mode, (width, new_height), (255, 255, 255))
    top = int((new_height - height) / 2)
    result.paste(image, (0, top))
    result.save(image.filename)



def resize_image():
    for (root, dirs, files) in os.walk(BASE_DIR / 'media/src/'):
        for file in files:
            path = Path(root) / file

            try:
                with Image.open(path) as image:
                    shutil.copy(image.filename, BASE_DIR / 'media/dest/' / file)
            except UnidentifiedImageError as e:
                print(e)

    for (root, dirs, files) in os.walk(BASE_DIR / 'media/dest/'):
        for file in files:
            path = Path(root) / file
            try:
                with Image.open(path) as image:
                    if image.height > image.width:
                        print(f"height is larger than width: {path}")
                        continue
                    if image.width != 800:
                        resize_by_width(image, 800)
                    increase_height(image, 800)
            except UnidentifiedImageError as e:
                print(e)


if __name__ == '__main__':
    resize_image()
