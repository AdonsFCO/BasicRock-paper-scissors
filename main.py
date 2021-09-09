import pygame
import random




running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
hands = pygame.image.load('Draws/Pager rock and sissors .png')

def drawhands(x, y):
    screen.blit(hands, (x, y))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawhands(0, 0)
    pygame.display.update()



