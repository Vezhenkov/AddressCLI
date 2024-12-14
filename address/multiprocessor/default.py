import multiprocessing


class MultiprocessorDefault:
    def __init__(self, targets):
        self.targets = targets
        self.execution_time = 0

    def get(self):
        processes = min(multiprocessing.cpu_count(), len(self.targets))
        with multiprocessing.Pool(processes) as p:
            targets_dataset, time = zip(*p.map(self.fn, self.targets))
            self.execution_time = max(time)
            return targets_dataset

    @staticmethod
    def fn(*args):
        return args[0].get(), args[0].execution_time
