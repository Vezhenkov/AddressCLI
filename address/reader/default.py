import os

import pandas


class ReaderDefault:
    def __init__(self, client_input):
        self.client_input = client_input
        self.valid_extensions = ['.txt']

    def get(self):
        with open(self.client_input.get()) as f:
            return pandas.DataFrame(f.readlines())

    def isFilePathValid(self):
        file_extension = os.path.splitext(self.client_input.get())[1]
        return file_extension in self.valid_extensions
