"""An helper class for parsing CSV file.

The class inherits the IngestorInterface.
The class depends on the pandas library to complete the defined,
abstract method signatures to parse CSV files.
The parse method returns a valid QuoteModel.
"""
from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import sys
import os


class CSVIngestor(IngestorInterface):
    """CSVIngestor class for parsing CSV file.

    Inherits the IngestorInterface.
    Class method `parse`: Reads the data from CSV file
    and returns a list of QuoteModel.
    """

    allowed_file_types = ['csv']

    @classmethod
    def parse(cls, path: str):
        """To read data from CSV file.

        :param path: Path to the quote file.
        :return: List of QuoteModel.
        Quits the script if any exception occurs while
        opening or reading data from file.
        """
        if not cls.can_ingest(path):
            raise Exception("Input file can not be ingested")
        try:
            quotes = []
            df = pandas.read_csv(path, header=0)
            for index, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
            return quotes
        except Exception as e:
            exc_type, exc_msg, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception Type: {exc_type}\nFile: {fname}\nLine Number:\
                   {exc_tb.tb_lineno}\nError: {exc_msg}")
            sys.exit(1)
