import pygame
import random
def drawhands(x, y):
    #screen.blit(handsOriginalResolution, (x, y))
    #screen.blit(black, (x, y))
    #screen.blit(paper, (x, y))
    screen.blit(sissors,(x,y))
def chopTwice(surface):
    newSurface = pygame.transform.chop(surface,(0,0,100,0))
    newSurface = pygame.transform.chop(newSurface,(130,0,450,0))
    return newSurface



running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
handsOriginalResolution = pygame.image.load('Draws/tiny .png')
#tinyHands = pygame.transform.scale(handsOriginalResolution,(380, 161))
#(x,y,w,h) represents a rectangle with top left point at (x,y), with width w and height h.
test = pygame.image.load('Draws/SampleTest.png')
#rock = pygame.transform.chop(handsOriginalResolution, (20, 20, 20, 20))
sissors = chopTwice(handsOriginalResolution)
#paper = pygame.transform.chop(handsOriginalResolution,(0,0,220,0))
#black = pygame.transform.chop(test,(0,0,250,0))





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((10, 200, 3))
    drawhands(200, 450)
    pygame.display.update()



