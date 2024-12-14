class ClientOutputDefault:
    def __init__(self, counter):
        self.counter = counter

    def get(self):
        counter_dataset = self.get_counter_dataset()
        output = '\n'
        for counter_data in counter_dataset:
            output += f'{counter_data.to_string(index=False)}\n\n'
        output += 'Processing time: {:.2}'.format(float(self.counter.execution_time))
        return output

    def get_counter_dataset(self):
        counter_dataset = self.counter.get()
        if not hasattr(counter_dataset, "__len__"):
            counter_dataset = (counter_dataset,)
        return counter_dataset
