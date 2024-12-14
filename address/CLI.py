from .client_input.default import ClientInputDefault
from .reader.selective import ReaderSelective
from .counter.multi import CounterMulti
from .client_output.default import ClientOutputDefault


class CLI:
    def __init__(self):
        self.client_input = ClientInputDefault()
        self.reader = ReaderSelective(self.client_input)
        self.counter = CounterMulti(self.reader)
        self.client_output = ClientOutputDefault(self.counter)

    def get(self):
        print(self.client_output.get())
