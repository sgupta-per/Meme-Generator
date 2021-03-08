"""Class for Flask app starter code.

The script uses the Quote Engine module and Meme Generator modules
to generate a random captioned image.
This script uses the requests package to fetch an image from a user
submitted URL.

Example:
`$ python3 app.py`
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request, make_response
from QuoteEngine import QuoteModel, Ingestor
from MemeGen import MemeEngine

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
meme = MemeEngine('./static')


def setup():
    """Define method to load all resources.

    :return: quotes
    :return: imgs
    This method parses all quote files and saves returns a list of
    QuoteModel for dog, cat, and horse.
    Returns the list of images from image diretory.
    e.g. "./_data/photos/"
    """
    images_path = "./_data/photos/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        imgs = [os.path.join(root, name) for name in files]
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.

    Uses the random python standard library class to:
        1. select a random image from imgs array
        2. select a random quote from the quotes array

    Uses amazon_rekognition_api to identify content of an image,
    if the image content is Dog/Cat/Horse, it will use respective
    quote files.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    1. Uses requests to save the image from the image_url.
    2. Saves image to a local temp file.
    3. Uses the meme object to generate a meme using this temp
       file and the body and author form paramaters.
    3. Remove the temporary saved image.
    """
    image_url = request.form['image_url']
    quote_body = request.form['body']
    quote_author = request.form['author']
    response = requests.get(image_url)
    tmp_image = "./tmp/tmp.png"
    file = open(tmp_image, "wb")
    file.write(response.content)
    file.close()
    path = meme.make_meme(tmp_image, quote_body, quote_author)
    os.remove(tmp_image)
    return render_template('meme.html', path=path)


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('404.html', path='./static/opps.png'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500


@app.after_request
def add_header(response):
    """To handle cache problems in browser."""
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response


if __name__ == "__main__":
    """Starting Flask Server."""
    app.run()
