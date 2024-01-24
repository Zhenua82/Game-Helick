from utils import randbool

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update(self, cut = 1, max = 20, cut2 = 1, max2 = 10):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(cut, max):
                    self.cells[i][j] = 1
                    if randbool(cut2, max2):
                        self.cells[i][j] = 2
                else: self.cells[i][j] = 0

    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]
