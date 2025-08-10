import pygame

COLUMNS, ROWS, SIZE = 30,20,30

class Tile:
    def __init__(self, name, collidable, image = None):
        self.name = name
        self.collidable = collidable
        self.image = image

def fill_tiles():
    positions = [[Tile("Blank", "False")] * COLUMNS for i in range(0,ROWS)]

    grassTile = Tile("Grass", False)
    rockTile = Tile("Rock", True)
    dirtTile = Tile("Dirt", False)
    waterTuke = Tile("Water", True)

    #Left Forest Area Trees
    for i in range(0, 15):
        positions[0][i] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(0, ROWS):
        positions[j][0] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for i in range(0, 20):
        positions[ROWS-1][i] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for i in range(5, 10):
        for j in range(5, 12):
            positions[j][i] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(1, 6):
        positions[j][14] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(5, 8):
        positions[j][15] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(10, 13):
        positions[j][15] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(12, 16):
        positions[j][16] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(15, 17):
        positions[j][17] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(16, 18):
        positions[j][18] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())
    for j in range(17, 20):
        positions[j][19] = Tile("Tree", True, pygame.image.load("tiles/tree.png").convert())

    #Left Forest Area Grass
    for i in range(1, 5):
        for j in range(1, ROWS-1):
            positions[j][i] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for i in range(5, 14):
        for j in range(1, 5):
            positions[j][i] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for i in range(5, 14):
        for j in range(12, ROWS-1):
            positions[j][i] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for i in range(10, 14):
        for j in range(5,12):
            positions[j][i] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(6, 19):
        positions[j][14] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(13, 19):
        positions[j][15] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(16, 19):
        positions[j][16] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(17, 19):
        positions[j][17] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(18, 19):
        positions[j][18] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())
    for j in range(8, 10):
        positions[j][15] = Tile("Grass", False, pygame.image.load("tiles/grass.png").convert())

    #Top-River
    for i in range(15, 18):
        for j in range(0, 5):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(16, 19):
        for j in range(3, 8):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())

    #Bridge
    for i in range(15, 19):
        positions[8][i] = Tile("Top-Bridge", False, pygame.image.load("tiles/top_bridge.png").convert_alpha())
    for i in range(15, 19):
        positions[9][i] = Tile("Bottom-Bridge", False, pygame.image.load("tiles/bottom_bridge.png").convert_alpha())

    #Bottom-River
    for i in range(16, 19):
        for j in range(10, 12):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(17, 20):
        for j in range(10, 15):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(18, 21):
        for j in range(14, 16):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(19, 22):
        for j in range(15, 17):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(22, 23):
        positions[16][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())
    for i in range(20, COLUMNS):
        for j in range(17, ROWS):
            positions[j][i] = Tile("Water", True, pygame.image.load("tiles/water.png").convert())

    #Mountains
    for i in range(18, 25):
        positions[0][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(27, 30):#
        positions[0][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(18, 24):
        positions[1][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(27, 30):#
        positions[1][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(18, 24):
        positions[2][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(26, 30):#
        positions[2][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(19, 23):
        positions[3][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(26, 30):#
        positions[3][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(19, 23):
        positions[4][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(25, 30):#
        positions[4][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(19, 22):
        positions[5][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(25, 30):#
        positions[5][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(19, 21):
        positions[6][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(24, 30):#
        positions[6][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(19, 20):
        positions[7][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(23, 30):#
        positions[7][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(22, 30):#
        positions[8][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(23, 30):#
        positions[9][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(20, 21):
        positions[10][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(24, 30):#
        positions[10][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(20, 22):
        positions[11][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(26, 30):#
        positions[11][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(20, 23):
        positions[12][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(20, 24):
        positions[13][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(21, 30):
        positions[14][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(22, 30):
        positions[15][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())
    for i in range(23, 30):
        positions[16][i] = Tile("Mountain", True, pygame.image.load("tiles/mountain.png").convert())


    #Dirt
    #19-22, 21-23, 23-30, 24-30,
    for i in range(25,27):
        positions[0][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(24,27):
        positions[1][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(24,27):
        positions[2][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(23,26):
        positions[3][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(23,25):
        positions[4][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(22,25):
        positions[5][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(21,24):
        positions[6][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(20,23):
        positions[7][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(19,22):
        positions[8][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(19,23):
        positions[9][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(21,24):
        positions[10][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(22,26):
        positions[11][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(23,30):
        positions[12][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())
    for i in range(24,30):
        positions[13][i] = Tile("Dirt", False, pygame.image.load("tiles/dirt.png").convert())

    return positions


