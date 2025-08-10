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

x = 13
y = 10

positions = tile.fill_tiles()

character = pygame.image.load("tiles/character.png").convert_alpha()

direction = ""
movement_counter = 0

while running:

    screen.fill((255,255,255))

    for i in range(0, COLUMNS):
        for j in range(0, ROWS):
            if positions[j][i].image:
                screen.blit(positions[j][i].image, (i*SIZE, j*SIZE))

    screen.blit(character, (x*SIZE, (y*SIZE)-(SIZE/2)))

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