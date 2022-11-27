import file 
class packet:
    def __init__(self):
        self.data = None
    
    def set_data(self, data):
        self.data = data

    def show_content(self):
        print(self.data)

    def return_content(self):
        return self.data
