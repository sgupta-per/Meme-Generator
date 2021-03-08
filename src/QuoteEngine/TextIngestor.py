"""An helper class for parsing TXT file.

The class inherits the IngestorInterface.
The parse method returns a valid QuoteModel.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import sys
import os


class TextIngestor(IngestorInterface):
    """TextIngestor class for parsing TXT file.

    Inherits the IngestorInterface.
    Class method `parse`: Reads the data from TXT file and
    returns a list of QuoteModel.
    """

    allowed_file_types = ['txt']

    @classmethod
    def parse(cls, path: str):
        """To read data from TXT file.

        :param path: Path to the quote file.
        :return: List of QuoteModel.
        Quits the script if any exception occurs while opening
        or reading data from file.
        """
        if not cls.can_ingest(path):
            raise Exception("Input file can not be ingested")
        try:
            quotes = []
            with open(path, 'r') as infile:
                for line in infile:
                    line = line.split('-')
                    new_quote = QuoteModel(line[0], line[1])
                    quotes.append(new_quote)
                return quotes
        except Exception as e:
            exc_type, exc_msg, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception Type: {exc_type}\nFile: {fname}\nLine Number:\
                   {exc_tb.tb_lineno}\nError: {exc_msg}")
            sys.exit(1)
