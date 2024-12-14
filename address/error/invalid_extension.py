import os

from .default import ErrorDefault


class ErrorInvalidExtension(ErrorDefault):
    def __init__(self, target):
        self.target = target
        super().__init__(os.path.splitext(self.target.get())[1][1:])
