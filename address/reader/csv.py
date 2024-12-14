import os

import pandas

from .default import ReaderDefault


class ReaderCSV(ReaderDefault):
    def __init__(self, client_input):
        super().__init__(client_input)
        self.valid_extensions = ['.csv']

    def get(self):
        return pandas.read_csv(self.client_input.get(), sep=";")
