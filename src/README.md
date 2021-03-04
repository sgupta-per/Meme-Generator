## Overview

At high level this project contains the code for a 'Meme Generator', a multimedia application to dynamically generate memes, including an image with an overlaid quote.

The main fuctions that this application provides:
- It interacts with different file types (PDF, Word Documents, CSVs, Text files) and loads quotes from these files.
- It loads, manipulates, and saves images.
- It uses Amazon Rekognition to identify contents of a image and chooses the image category.
- Provides Meme Generator application through a command line tool and a web service.
- Accept dynamic user input through a command-line tool and a web service.

<!-- ## Things required
As for Ramdom meme generation this project uses Amazon api to identify image contents,
so this requires valid access id and key to defined in `amazon_rekognition_api.py` file.
e.g.
ACCESS_ID = "AKIA4545343V7IY6I4QPZ"
ACCESS_KEY = "8+uH1BzQ2X34434343RQrgO5PSIV5V9hXOquypimh2n" -->

## Understanding different files and diretories

- `meme.py`: The main Python script that wraps the command-line tool, orchestrates the data pipeline by invoking the functions and classes.
- `app.py`: The main Python script to launch web service, this file uses other functions and classes for Meme Generation.
<!-- - `amazon_rekognition_api.py`: This file contains the code for Amazon api call, used in `meme.py` and `app.py` for ramdom meme generation. -->
This project uses two modules,
-- `QuoteEngine` for quote engine
    -- `IngestorInterface.py`: An abstract base class, it defines two methods with the following class method       signatures:
                def can_ingest(cls, path: str) -> boolean
                def parse(cls, path: str) -> List[QuoteModel]
    -- `Ingestor.py`: A final Ingestor class realizes the IngestorInterface abstract base class and encapsulate     helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.
    -- `CSVIngestor.py`: Helper class to parse CSV files.
    -- `DocxIngestor.py`: Helper class to parse docx files.
    -- `PDFIngestor.py`: Helper class to parse pdf files.
    -- `TextIngestor.py`: Helper class to parse text files.
    -- `QuoteModel.py`: Provides a QuoteModel object with body and author.
-- `MemeGen` for meme engine
    -- `MemeEngine.py`: Class to generate a captioned image. This class has following responsibilities. This class uses `BodoniBold.ttf` and `bodoni.ttf` files for font style.
        -- Loading of a file from disk
        -- Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
        -- Add a caption to an image (string input) with a body and author to a random location on the image.
-- Data files are located in folder `_data`

# How to use
-- Run from command-line
`$ python3 meme.py`
`$ python3 meme.py --path './_data/photos/Image10.jpeg' --body 'Test quote' --author 'Shivani'`

-- For Web-service
`$ python3 app.py`
Web-service will be launched at `http://127.0.0.1:5000/`