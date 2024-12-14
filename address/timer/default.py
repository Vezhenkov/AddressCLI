import time


class TimerDefault(type):
    def __init__(cls, clsname, superclasses, attributedict):
        super().__init__(clsname, superclasses, attributedict)
        default_get = cls.get

        def patched_get(self):
            t1 = time.time()
            res = default_get(self)
            t2 = time.time()
            self.execution_time = t2 - t1
            return res

        cls._default_get = default_get
        cls.get = patched_get
