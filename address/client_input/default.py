class ClientInputDefault:
    def __init__(self):
        self.prompt = 'Supported formats: .csv, .xml\nFile path: '

    def get(self):
        return input(self.prompt)
