from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        coordinates = randcell(self.w, self.h)
        x, y = coordinates[0], coordinates[1]
        self.x = y
        self.y = x
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20

    def move(self, x, y):
        coordinates_x, coordinates_y = self.x + x, self.y + y
        if (coordinates_x >= 0) and (coordinates_y >= 0) and (coordinates_x < self.h) and (coordinates_y < self.w):
            self.x, self.y = coordinates_x, coordinates_y

    def print_stats(self):
        print('🧺 ', self.tank,'/',self.mxtank, sep = '', end = ' | ')
        print('🏆', self.score, end = ' | ')
        print('🧡', self.lives)

    def game_over(self):
        os.system('cls')
        print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
        print('W                                 W')
        print('W GAME OVER, UOUR SCORE IS', self.score, '   W')
        print('W                                 W')
        print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
        exit(0)

    def export_data(self):
        return {'score': self.score, 'lives': self.lives, 
                'x': self.x, 'y': self.y, 'tank': self.tank, 
                'mxtank': self.mxtank}
    
    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.score = data['score'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 5