from .default import TimerDefault


class TimerManual(TimerDefault):
    def __init__(cls, clsname, superclasses, attributedict):
        super().__init__(clsname, superclasses, attributedict)
        cls.get = cls._default_get
