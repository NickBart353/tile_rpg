import pygame
from pygame.draw_py import draw_line
import tile
from tile import Tile

pygame.init()

SIZE, COLUMNS, ROWS = tile.SIZE, tile.COLUMNS, tile.ROWS

screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock = pygame.time.Clock()

delta_time = 0
running = True

x = 10
y = 10

positions = tile.fill_tiles()

direction = ""
movement_counter = 0

while running:

    screen.fill((255,255,255))

    for i in range(0, COLUMNS):
        for j in range(0, ROWS):
            match positions[j][i].name:
                case "Blank":
                    pygame.draw.rect(screen, (200, 200, 200), (i * SIZE, j * SIZE, SIZE, SIZE))
                case "Tree":
                    pygame.draw.rect(screen, (0, 100, 0), (i * SIZE, j * SIZE, SIZE, SIZE))
                case "Grass":
                    pygame.draw.rect(screen, (0, 200, 0), (i * SIZE, j * SIZE, SIZE, SIZE))
                case "Rock":
                    pygame.draw.rect(screen, (150, 150, 150), (i * SIZE, j * SIZE, SIZE, SIZE))
                case "Water":
                    pygame.draw.rect(screen, (30, 150, 250), (i * SIZE, j * SIZE, SIZE, SIZE))
                case "Dirt":
                    pygame.draw.rect(screen, (135, 92, 5), (i * SIZE, j * SIZE, SIZE, SIZE))


    # for i in range(1, COLUMNS):
    #     pygame.draw.line(screen, (245,245,245), (i*SIZE,0), (SIZE*i, ROWS*SIZE))
    # for i in range(1, ROWS):
    #     pygame.draw.line(screen, (245,245,245), (0,i*SIZE), (COLUMNS*SIZE, SIZE*i))

    pygame.draw.rect(screen, (245,145,24), (x*SIZE,y*SIZE,SIZE,SIZE))


    while movement_counter > 0:
        movement_counter -= 1
        match direction:
            case "UP":
                if not (y-1 < 0) and not (positions[y-1][x].collidable == True):
                    y -= 1
            case "DOWN":
                if not (y+1 == ROWS) and not (positions[y+1][x].collidable == True):
                    y += 1
            case "LEFT":
                if not (x-1 < 0) and not (positions[y][x-1].collidable == True):
                    x -= 1
            case "RIGHT":
                if not (x + 1 == COLUMNS) and not (positions[y][x+1].collidable == True):
                    x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and movement_counter == 0:
                direction = "UP"
                movement_counter = 1
            if event.key == pygame.K_s and movement_counter == 0:
                direction = "DOWN"
                movement_counter = 1
            if event.key == pygame.K_a and movement_counter == 0:
                direction = "LEFT"
                movement_counter = 1
            if event.key == pygame.K_d and movement_counter == 0:
                direction = "RIGHT"
                movement_counter = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movement_counter = 0
            if event.key == pygame.K_s:
                movement_counter = 0
            if event.key == pygame.K_a:
                movement_counter = 0
            if event.key == pygame.K_d:
                movement_counter = 0

    delta_time = clock.tick(60) / 1000
    pygame.display.flip()
pygame.quit()