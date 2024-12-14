import os

import pandas

from .default import ReaderDefault


class ReaderXML(ReaderDefault):
    def __init__(self, client_input):
        super().__init__(client_input)
        self.valid_extensions = ['.xml']

    def get(self):
        return pandas.read_xml(self.client_input.get())
