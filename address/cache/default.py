class CacheDefault:
    def __init__(self, target):
        super().__init__()
        self.value = target.get()

    def get(self):
        return self.value
