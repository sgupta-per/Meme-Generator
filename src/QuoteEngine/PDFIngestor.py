"""An helper class for parsing PDF file.

The class inherits the IngestorInterface.
This class utilizes the subprocess module to call the pdftotext
CLI utility—creating a pipeline that converts PDFs to text and
then ingests the text.
The class handles deleting temporary files.
The parse method returns a valid QuoteModel.
"""
from typing import List
import subprocess
import os
import sys
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor class for parsing PDF file.

    Inherits the IngestorInterface.
    Class method `parse`: Reads the data from PDF file and returns
    a list of QuoteModel.
    """

    allowed_file_types = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """To read data from PDF file.

        :param path: Path to the quote file.
        :return: List of QuoteModel.
        Quits the script if any exception occurs while opening or
        reading data from file.
        """
        if not cls.can_ingest(path):
            raise Exception("Input file can not be ingested")
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, tmp])
            quotes = []
            with open(tmp, "r") as file_ref:
                for line in file_ref:
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        parse = line.split(' "')
                        for item in parse:
                            item = item.split('-')
                            new_quote = QuoteModel(item[0], item[1])
                            quotes.append(new_quote)
            os.remove(tmp)
            return quotes
        except Exception as e:
            exc_type, exc_msg, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception Type: {exc_type}\nFile: {fname}\nLine Number:\
                   {exc_tb.tb_lineno}\nError: {exc_msg}")
            sys.exit(1)
