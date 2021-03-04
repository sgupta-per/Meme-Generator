"""Represents an abstract base class.

Which defines methods to validate if provided input file
can be ingested and another method to parse the input
file provided.
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface abstract base class.

    Define a list `allowed_file_types` of all allowed file types.
    Class method `can_ingest` to check given input file can be ingested.
    Class method `parse` for use in individual ingestor class of each
    file type.
    """

    allowed_file_types = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Validate if a given quote file type is supported.

        :param path: Path to quote file.
        :return: boolen True or False
        Return true if file type is present in allowed_file_types,
        and False if not.
        """
        file_type = path.split('.')[-1]
        return file_type in cls.allowed_file_types

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parsing the file content.

        An abstract method for parsing the file content (i.e.,
        splitting each row)
        and outputting it to a Quote object.
        """
        pass
