"""Main Ingestor class.

All ingestors are packaged into this Ingestor class.
This class encapsulates all the ingestors to provide one
interface to load any supported file type.
"""
from typing import List
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Ingestor class.

    This class encapsulates all the ingestors to provide one
    interface to load any supported file type.
    """

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str):
        """To provide a interface to load a supported filetype.

        This method validates if a given file type is supported and
        provides a interface to load given file type if supported.

        e.g.
        for .pdf file, it will return parse method object of PDFIngestor.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
