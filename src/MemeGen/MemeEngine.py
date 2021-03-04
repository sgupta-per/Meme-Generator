"""Meme Generator class.

It performs,
    -- Loading of a file from disk.
    -- Transform image by resizing to a maximum width of 500px
       while maintaining the input aspect ratio
    -- Add a caption to an image (string input) with a body
       and author to a random location on the image.
    -- The class depends on the Pillow library to complete the defined,
       incomplete method signatures so that they work with JPEG/PNG files.
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


class MemeEngine:
    """MemeEngine Class.

    This defines output diretory to save the generated captioned image.
    Defines method to create captioned image.
    """

    def __init__(self, out_dir):
        """Define output directory to save generated image."""
        self.out_dir = out_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate captioned image.

        :param img_path: Path to input Image
        :param text: Quote body to add to the image
        :param author: Quote author to add to the image
        :param width: Image width default to 500
        :return: path to generated captioned image.

        Uses the Pillow library to perform basic image operations.
        Uses `BodoniBold.ttf` and `bodoni.ttf` files for fonts.
        """
        offsets = [(10, 20), (100, 200), (100, 300), (10, 400),
                   (150, 250), (40, 100)]
        img = Image.open(img_path)
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        quote = f"{text} \n - {author}"
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("BodoniBold.ttf", 25)
        font1 = ImageFont.truetype("bodoni.ttf", 20)
        xoff, yoff = random.choice(offsets)
        draw.text((xoff, yoff), text, font=font, fill='black')
        draw.text((xoff, yoff + 30), f"    - {author}", font=font1,
                  fill='black')
        img_format = img_path.split('.')[-1]
        meme_path = f"{self.out_dir}/out.{img_format}"
        img.save(meme_path)
        return meme_path
