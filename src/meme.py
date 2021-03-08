"""Generate Meme - Command-line.

This script uses QuoteModel, Ingestor and MemeEngine classes to
to generate a random captioned image.

The program takes three OPTIONAL arguments:
-- A string quote body
-- A string quote author
-- An image path
The program returns a path to a generated image.
If any argument is not defined, a random selection is used.
    Examples to run script:

    -- python3 meme.py

    -- python3 meme.py --path './_data/photos/dog/xander_1.jpg'
       --body 'Test quote' --author 'Shivani'
"""
import os
import random
import argparse

from QuoteEngine import QuoteModel, Ingestor
from MemeGen import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote.

    :param path: Path to the image file
    :param body: Quote body to add to the image.
    :param author: Quote author to add to the image.
    :return: Path to the generated image

    This function generates meme using the image and quote content given
    in command line arguments.
    If arguments are not given, it will choose image and quote based on
    random selection from directories and files defined within the function.
    e.g. For images, its using directory "./_data/photos/"
    For quotes './_data/DogQuotes/DogQuotesTXT.txt' etc.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/"
        imgs = []
        for root, dirs, files in os.walk(images):
            if '.DS_Store' in files:
                files.remove('.DS_Store')
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path
    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel.QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(
        description="Generate Meme"
    )
    parser.add_argument('--path', default=None, help="Path to image file.")
    parser.add_argument('--body', default=None,
                        help="Quote body to add to the image.")
    parser.add_argument('--author', default=None,
                        help="Quote author to add to the image.")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
