class IngestionException(Exception):
    pass


class UnsupportedFileTypeError(
    IngestionException
):
    pass


class FileTooLargeError(
    IngestionException
):
    pass


class DuplicateDocumentError(
    IngestionException
):
    pass


class EmptyDocumentError(
    IngestionException
):
    pass