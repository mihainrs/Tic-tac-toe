import pygame
import time

#variables and stuff


#initializing screen
pygame.display.init()
size = (800, 600) #w, h
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption('Tic Tac Toe!')

game_running = True

#getting the window to stay active / initializing game loop
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False


    #lines for the game/field
    pygame.draw.line(screen, (0,0,0), (250,600), (250,0), 5)
    pygame.draw.line(screen, (0,0,0), (550,600), (550,0), 5)
    pygame.draw.line(screen, (0,0,0), (800,200), (0,200), 5)
    pygame.draw.line(screen, (0,0,0), (800,400), (0,400), 5)
    pygame.display.flip()