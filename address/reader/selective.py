from .default import ReaderDefault
from .csv import ReaderCSV
from .xml import ReaderXML
from ..cache.default import CacheDefault
from ..error.invalid_extension import ErrorInvalidExtension


class ReaderSelective(ReaderDefault):
    def __init__(self, client_input):
        super().__init__(client_input)
        self.reader_classes = [ReaderCSV, ReaderXML]
        self.valid_extensions = ['.csv', '.xml']

    def get(self):
        cached_client_input = CacheDefault(self.client_input)
        for reader_class in self.reader_classes:
            reader = reader_class(cached_client_input)
            if reader.isFilePathValid():
                return reader.get()
        raise ErrorInvalidExtension(cached_client_input)
