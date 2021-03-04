"""Define QuoteModel object.

With quote body and its author.
"""


class QuoteModel:
    """Python class that defines a QuoteModel object.

    which contains text fields for body and author.
    The class overrides the correct methods to instantiate the
    class and print the model contents as: ”body text” - author
    """

    def __init__(self, body, author):
        """__init__ method.

        Defines quote body and its author.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f"{self.body} - {self.author}"
