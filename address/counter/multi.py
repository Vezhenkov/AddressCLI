from ..timer.manual import TimerManual
from ..counter.default import CounterDefault
from ..counter.duplicates import CounterDuplicates
from ..counter.floor import CounterFloor
from ..cache.default import CacheDefault
from ..multiprocessor.default import MultiprocessorDefault


class CounterMulti(CounterDefault, metaclass=TimerManual):
    def __init__(self, reader):
        super().__init__(reader)
        self.target_classes = [CounterFloor, CounterDuplicates]
        self.execution_time = 0

    def get(self):
        cached_reader = CacheDefault(self.reader)
        targets = [counter(cached_reader) for counter in self.target_classes]
        multiprocessor = MultiprocessorDefault(targets)
        targets_dataset = multiprocessor.get()
        self.execution_time = multiprocessor.execution_time
        return targets_dataset
