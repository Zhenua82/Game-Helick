from map import Map
from helicopter import Helicopter as Helico
import time
import os
from pynput import keyboard
from clouds import Clouds
import json

# управление вертолетом
def process_key(key):
    global helico, tick, clouds, field
    button = key.char.lower()
    if button in MOVES.keys():
        x, y = MOVES[button][0], MOVES[button][1]
        helico.move(x, y)
    # сохранение игры
    elif button == 'f':
        data = {'helicopter': helico.export_data(), 
                'clouds': clouds.export_data(), 
                'field': field.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    # загрузка игры
    elif button == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            helico.import_data(data['helicopter'])
            tick = data['tick'] or 1
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])

listener = keyboard.Listener(
    on_press = process_key,
    on_release = None)
listener.start()

MAP_W, MAP_H = 22, 12
TICK_SLEEP = 0.05
TREE_UPDATE = 40
FIRES_UPDATE = 40
MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)}
CLOUDS_UPDATE = 150

clouds = Clouds(MAP_W, MAP_H)
field = Map(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
tick = 1
while True:
    os.system('cls') #очищает
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print('TICK', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRES_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()
