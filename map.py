from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.WW.......W',
    'W......W...W',
    'W..........W',
    'W..........W',
    'W....WWWW..W',
    'WW.........W',
    'WWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))