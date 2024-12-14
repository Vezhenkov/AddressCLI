from ..timer.default import TimerDefault


class CounterDefault(metaclass=TimerDefault):
    def __init__(self, reader):
        self.reader = reader
        self.execution_time = 0

    def get(self):
        reader_data = self.reader()
        amount = reader_data[reader_data.columns[0]].count()
        return amount
