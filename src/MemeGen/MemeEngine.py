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
import textwrap


class MemeEngine:
    """MemeEngine Class.

    This defines output diretory to save the generated captioned image.
    Defines method to create captioned image.
    Defines method to wrap quote text.
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
        try:
            image = Image.open(img_path)
        except IOError as e:
            print(e)
        # Set width to default 500 if given width is greater than 500
        if width > 500:
            width = 500
        ratio = width/float(image.size[0])
        height = int(ratio*float(image.size[1]))
        image = image.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("BodoniBold.ttf", 25)
        font1 = ImageFont.truetype("bodoni.ttf", 20)
        xoff, yoff = random.choice(offsets)
        # Call function to wrap text
        lines = self.text_wrap(text, font, image.size[0]-xoff)
        # Define line height based on char h and g
        line_height = font.getsize('hg')[1]
        for line in lines:
            draw.text((xoff, yoff), line, font=font, fill='black')
            yoff = yoff + line_height
        draw.text((xoff, yoff + 20), f"    - {author}", font=font1,
                  fill='black')
        img_format = img_path.split('.')[-1]
        meme_path = f"{self.out_dir}/out.{img_format}"
        image.save(meme_path)
        return meme_path

    def text_wrap(self, text, font, max_width):
        """Wrap text based on given width.

        This function breaks the text to multi-line text if given
        text is long and its crossing the edges of an image.
        :param text: Text to be wrapped
        :param font: Font type
        :param max_width: Desired width for the text
        :return: List of sub-strings
        """
        lines = []
        # No need to split if text width is smaller than max_width
        if font.getsize(text)[0] <= max_width:
            lines.append(text)
        else:
            # Splitting the line by space to get the list of words
            words = text.split(' ')
            i = 0
            # append word to a line while its width is shorter than
            # the max_width
            while i < len(words):
                line = ''
                while (i < len(words) and
                       font.getsize(line + words[i])[0] <= max_width):
                    line = line + words[i] + ' '
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines
