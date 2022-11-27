from math import ceil
from Storage import Storage
from Packetize import packetize
from Packetize import PACKET_SIZE
from file import file
from map import map

class network:
    def __init__(self):
        self.storages = []
        self.storages_index = 0
        self.data_record_tracker = 0
        self.map = None
    
    def set_storages(self, storages, map):
        # for i in storages:
        #     if isinstance(i, Storage):
        #         self.storages.append(i)
        #     else:
        #         raise ValueError(i, 'is not a storage server!')
        if isinstance(storages, list):
            if all(isinstance(s, Storage) for s in storages):
                self.storages = storages
                self.map = map
                return
        raise ValueError(storages, 'is not a list of storage servers!')

    def send_data(self, data):
        tmp = file()
        tmp.record(None,"data_record_"+str(self.data_record_tracker))
        self.map.record(tmp, self.storages_index, self.storages[self.storages_index].next_file_index())
        packets = packetize(data)
        for i, p in enumerate(packets):
            self.storages[self.storages_index].store(p)
            self.storages_index = (self.storages_index + 1) % self.storages.__len__()
        
        # self.storages_index = (self.storages_index +1) % self.storages.__len__()




    def send_file(self, _file):
        if not isinstance(_file, file):
            raise ValueError("this is not a file!")

        self.map.record(_file, self.storages_index, self.storages[self.storages_index].next_file_index())
        data = _file.data
        packets = packetize(data)
        for i, p in enumerate(packets):
            self.storages[self.storages_index].store(p)
            self.storages_index = (self.storages_index + 1) % self.storages.__len__()
        
        # self.storages_index = (self.storages_index +1) % self.storages.__len__()

    def retrieve_file(self, file_name):
        if not file_name in self.map.dict.keys():
            raise ValueError("file does not exist")
        
        start_storage, file_data_length, file_index = self.map.dict[file_name]
        counter = ceil(file_data_length / PACKET_SIZE)
        start_tmp = start_storage
        for i, j in enumerate(range(start_storage, start_storage + counter)):
            if j % self.storages.__len__() == 0 and i != 0:
                file_index += 1
                # start_storage = 1
            print(self.storages[j % self.storages.__len__() ].retrieve(file_index).return_content(), end='')

        print()