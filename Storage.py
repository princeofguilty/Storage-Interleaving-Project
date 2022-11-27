import packets

class Storage:
    def __init__(self):
        self.Data = []
        pass

    def next_file_index(self):
        return self.Data.__len__()
    
    def store(self, data):
        if isinstance(data, packets.packet):
            self.Data.append(data)
        else:
            raise Exception('A storage can only store packets')

    def show_content(self):
        print(self)
        for i in self.Data:
            i.show_content()

    def retrieve(self, index):
        return self.Data[index]