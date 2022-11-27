class file:
    def __init__(self, data = None, name = None):
        self.record(data, name)

    def record(self, data, name):
        self.name = name
        if(data is None):
            self.size = 0
        else:
            self.size = len(data)
        self.data = data