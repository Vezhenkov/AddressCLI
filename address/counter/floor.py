from .default import CounterDefault


class CounterFloor(CounterDefault):
    def __init__(self, reader):
        super().__init__(reader)
        self.column_names = ["city", "floor"]
        self.execution_time = 0

    def get(self):
        reader_data = self.reader.get()
        return reader_data.groupby(self.column_names, as_index=False).size().rename(columns={'size': 'amount'})
