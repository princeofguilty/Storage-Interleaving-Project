import Storage, file
class map:
    def __init__(self):
        self.dict = {}
    def record(self, file, storage_index, file_index):
        self.dict[file.name] = (storage_index, len(file.data), file_index)