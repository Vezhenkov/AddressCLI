from .default import CounterDefault


class CounterDuplicates(CounterDefault):
    def __init__(self, reader):
        super().__init__(reader)
        self.execution_time = 0

    def get(self):
        reader_data = self.reader.get()
        grouped_data = reader_data.groupby(reader_data.columns.tolist(), sort=False, as_index=False).size()
        return grouped_data[grouped_data['size'] != 1].rename(columns={'size': 'duplicates'})
