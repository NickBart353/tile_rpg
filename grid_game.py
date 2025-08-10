import pygame
from pygame.draw_py import draw_line
import tile
from tile import Tile

def click_button():
    m_running = False
    g_running = True
    return m_running, g_running

pygame.init()
pygame.mixer.init()

play_button_sound = pygame.mixer.Sound("sounds/Accept.wav")
quit_button_sound = pygame.mixer.Sound("sounds/Cancel.wav")
main_music = pygame.mixer.Sound("sounds/03 - Definitely Our Town.wav")
bump_sound = pygame.mixer.Sound("sounds/hurt.wav")

SIZE, COLUMNS, ROWS = tile.SIZE, tile.COLUMNS, tile.ROWS

screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))
clock = pygame.time.Clock()

delta_time = 0
running = True
menu_running = True
game_running = False

x = 13
y = 10

positions = tile.fill_tiles()

character = pygame.image.load("tiles/character.png").convert_alpha()

animation_counter = 1
animation_window_size = [COLUMNS*SIZE, ROWS*SIZE]

button_font = pygame.font.Font(None, 45)
title_font = pygame.font.Font(None, 60)

direction = ""
movement_counter = 0
movement_timer = 0
just_moved = False
last_moved_timer = 0
movement_speed = 200

while running:

    while menu_running:

        #menu
        pygame.draw.rect(screen,(50,50,50), (0,0,COLUMNS*SIZE,ROWS*SIZE))
        title_text =  title_font.render("Tile explorer!!!", True, (130, 255, 100))
        title_text_pos = title_text.get_rect(centerx=screen.get_width() / 2, y=50)
        screen.blit(title_text, title_text_pos)

        #start button
        start_button_rect = pygame.Rect((COLUMNS*SIZE)//9.5,(ROWS*SIZE)//3, (COLUMNS*SIZE)//4, 100)
        start_button_collision = start_button_rect.collidepoint(pygame.mouse.get_pos())
        start_button = pygame.draw.rect(screen, (255, 30, 100*start_button_collision), start_button_rect)

        start_button_text = button_font.render("Play game!", True, (220,220,220))
        start_button_text_pos = start_button_text.get_rect(centerx=(COLUMNS*SIZE)//5,y=(ROWS*SIZE)//2.5)
        screen.blit(start_button_text, start_button_text_pos)

        #quit button
        quit_button_rect = pygame.Rect((COLUMNS*SIZE)//1.5, (ROWS * SIZE) // 3, (COLUMNS * SIZE)// 4, 100)
        quit_button_collision = quit_button_rect.collidepoint(pygame.mouse.get_pos())
        quit_button = pygame.draw.rect(screen, (55, 30*quit_button_collision, 100), quit_button_rect)

        quit_button_text = button_font.render("Quit game!", True, (220,220,220))
        quit_button_text_pos = quit_button_text.get_rect(centerx=(COLUMNS*SIZE)//1.3, y=(ROWS * SIZE) // 2.5)
        screen.blit(quit_button_text, quit_button_text_pos)

        if start_button_collision:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_running = False
                    game_running = True
                    play_button_sound.play()

        if quit_button_collision:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_running = False
                    running = False
                    quit_button_sound.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu_running = False

        delta_time = clock.tick(60) / 1000
        pygame.display.flip()

    while game_running:
        if not pygame.mixer.get_busy():
            main_music.play(-1,0,2000)

        screen.fill((255,255,255))

        for i in range(0, COLUMNS):
            for j in range(0, ROWS):
                if positions[j][i].image:
                    screen.blit(positions[j][i].image, (i*SIZE, j*SIZE))

        screen.blit(character, (x*SIZE, (y*SIZE)-(SIZE/2)))

        if movement_timer+movement_speed <= pygame.time.get_ticks() and not movement_timer == 0 and just_moved == False:
            movement_counter = 1
            movement_timer = pygame.time.get_ticks()
            just_moved = True
            last_moved_timer = pygame.time.get_ticks()

        if last_moved_timer+movement_speed <= pygame.time.get_ticks() and just_moved:
            just_moved = False

        while movement_counter > 0:
            movement_counter -= 1
            match direction:
                case "UP":
                    if not (y-1 < 0) and not (positions[y-1][x].collidable == True):
                        y -= 1
                    else:
                        bump_sound.play()
                case "DOWN":
                    if not (y+1 == ROWS) and not (positions[y+1][x].collidable == True):
                        y += 1
                    else:
                        bump_sound.play()
                case "LEFT":
                    if not (x-1 < 0) and not (positions[y][x-1].collidable == True):
                        x -= 1
                    else:
                        bump_sound.play()
                case "RIGHT":
                    if not (x + 1 == COLUMNS) and not (positions[y][x+1].collidable == True):
                        x += 1
                    else:
                        bump_sound.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and movement_counter == 0:
                    direction = "UP"
                    while last_moved_timer+movement_speed <= pygame.time.get_ticks() and just_moved == False:
                        movement_counter = 1
                        last_moved_timer = pygame.time.get_ticks()
                    movement_timer = pygame.time.get_ticks()
                if event.key == pygame.K_s and movement_counter == 0:
                    direction = "DOWN"
                    while last_moved_timer+movement_speed <= pygame.time.get_ticks() and just_moved == False:
                        movement_counter = 1
                        last_moved_timer = pygame.time.get_ticks()
                    movement_timer = pygame.time.get_ticks()
                if event.key == pygame.K_a and movement_counter == 0:
                    direction = "LEFT"
                    while last_moved_timer+movement_speed <= pygame.time.get_ticks() and just_moved == False:
                        movement_counter = 1
                        last_moved_timer = pygame.time.get_ticks()
                    movement_timer = pygame.time.get_ticks()
                if event.key == pygame.K_d and movement_counter == 0:
                    direction = "RIGHT"
                    while last_moved_timer+movement_speed <= pygame.time.get_ticks() and just_moved == False:
                        movement_counter = 1
                        last_moved_timer = pygame.time.get_ticks()
                    movement_timer = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    movement_counter = 0
                    movement_timer = 0
                if event.key == pygame.K_s:
                    movement_counter = 0
                    movement_timer = 0
                if event.key == pygame.K_a:
                    movement_counter = 0
                    movement_timer = 0
                if event.key == pygame.K_d:
                    movement_counter = 0
                    movement_timer = 0

        delta_time = clock.tick(60) / 1000
        pygame.display.flip()
pygame.mixer.quit()
pygame.quit()