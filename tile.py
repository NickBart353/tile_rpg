COLUMNS, ROWS, SIZE = 30,20,30

class Tile:
    def __init__(self, name, collidable):
        self.name = name
        self.collidable = collidable

def fill_tiles():
    positions = [[Tile("Blank", "False")] * COLUMNS for i in range(0,ROWS)]

    grassTile = Tile("Grass", False)
    rockTile = Tile("Rock", True)
    dirtTile = Tile("Dirt", False)
    waterTuke = Tile("Water", True)

    for i in range(0, 15):
        positions[0][i] = Tile("Tree", True)
    for i in range(15, 18):
        positions[0][i] = Tile("Water", True)
    for i in range(18, 30):
        positions[0][i] = Tile("Rock", True)
    for i in range(0, 1):
        positions[1][i] = Tile("Tree", True)
    for i in range(1, 16):
        positions[1][i] = Tile("Dirt", False)

    return positions


