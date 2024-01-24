from utils import randbool
from utils import randcell
from utils import randcell2


class Map:
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range (w)] for j in range(h)]
        self.generate_forest(30, 100)
        self.generate_ivers(7)
        self.generate_ivers(20)
        self.generate_upgradeshop()
        self.generate_hospital()
       
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.w or y >= self.h:
            return False
        return True
    
    def print_map(self, helico, clouds):
        print('⬛' * (self.w + 2))
        for i in range(self.h):
            print('⬛', end = '')
            for j in range(self.w):
                cell = self.cells[i][j]
                if(clouds.cells[i][j] == 1):
                    print('🌀', end = '')
                elif(clouds.cells[i][j] == 2):
                    print('⚡', end = '')
                elif (helico.x == i) and (helico.y == j):
                    print('🚁', end = '')
                elif cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end = '')
            print('⬛')
        print('⬛' * (self.w + 2))

    def generate_ivers(self, l):
        coordinates = randcell(self.w, self.h)
        x, y = coordinates[0], coordinates[1]
        self.cells[y][x] = 2
        while l > 0:
            coordinates_2 = randcell2(x, y)
            x2, y2 = coordinates_2[0], coordinates_2[1]
            if self.check_bounds(x2, y2):
                self.cells[y2][x2] = 2
                x, y = x2, y2
                l -= 1

    def generate_forest(self, cut, max):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(cut, max):
                    self.cells[i][j] = 1

    def generate_tree(self):
        coordinates = randcell(self.h, self.w)
        x, y = coordinates[0], coordinates[1]
        if self.cells[x][y] == 0:
            self.cells[x][y] = 1

    def generate_fires(self):
        coordinates = randcell(self.h, self.w)
        x, y = coordinates[0], coordinates[1]
        if self.cells[x][y] == 1:
            self.cells[x][y] = 3
    
    def update_fires(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.cells[i][j] == 3:
                    self.cells[i][j] = 0
        for i in range(10):
            self.generate_fires()

    def generate_upgradeshop(self):
        coordinates = randcell(self.w, self.h)
        x, y = coordinates[0], coordinates[1]
        self.cells[y][x] = 4

    def generate_hospital(self):
        coordinates = randcell(self.w, self.h)
        x, y = coordinates[0], coordinates[1]
        if self.cells[y][x] != 4:
            self.cells[y][x] = 5
        else: self.generate_hospital()

    def process_helicopter(self, helico, clouds):
        coordinates_helico = self.cells[helico.x][helico.y]
        coordinates_clouds = clouds.cells[helico.x][helico.y]
        if coordinates_helico == 2:
            helico.tank = helico.mxtank
        if (coordinates_helico == 3) and (helico.tank > 0):
            helico.tank -= 1
            self.cells[helico.x][helico.y] = 1
            helico.score += TREE_BONUS
        if (coordinates_helico == 4) and (helico.score >= UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.mxtank += 1 
        if (coordinates_helico == 5) and (helico.score >= LIVES_COST):
            helico.score -= LIVES_COST
            helico.lives += 10 
        if coordinates_clouds == 2:
            helico.lives -= 1
            if helico.lives == 0:
               helico.game_over()

    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]
            

CELL_TYPES = '🟩🌲🌊🔥🏭🏥'
TREE_BONUS = 100
UPGRADE_COST = 500
LIVES_COST = 1000  