from random import randint as rand

def randbool(cut, max):
    number = rand(0, max)
    return (number <= cut)

def randcell(h, w):
    coordinates_w = rand(0, w - 1)
    coordinates_h = rand(0, h - 1)
    return (coordinates_h, coordinates_w)

def randcell2(h, w):
    cell = rand(0, 7)
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]
    coordinates_x, coordinates_y = moves[cell][0], moves[cell][1]
    return (h + coordinates_y, w + coordinates_x)