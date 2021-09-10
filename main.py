import pygame
import random


# JUST FOR TESTING PROPOSES. It does what it says it blit the different hands in to the game.
#   def draw_hands(x, y):
#   screen.blit(handsOriginalResolution, (x, y))
#   screen.blit(black, (x, y))
#   screen.blit(paper, (x, y))
#   screen.blit(rock, (x, y))
#   pass
# =============================================METHODS==========================================
# ==============Image related Methods==============#
def chop_twice(surface, tuple1, tuple2):
    subsurface = pygame.transform.chop(surface, tuple1)
    sub_subsurface = pygame.transform.chop(subsurface, tuple2)
    return sub_subsurface


# ==============Image related Methods==============#
# ==============Hand related Methods==============#
def draw_hands(hand, x, y):
    if hand == "rock":
        screen.blit(rock, (x, y))
    elif hand == "paper":
        screen.blit(paper, (x, y))
    elif hand == "scissors":
        screen.blit(scissors, (x, y))


def draw_enemy_hand(surface):
    currentenemyhand = pygame.transform.flip(surface, False, True)


def generate_interface():
    draw_hands("rock", 200, 400)
    draw_hands("paper", 300, 400)
    draw_hands("scissors", 500, 400)
    draw_enemy_hand(paper)

# =============================================IMPORTANT VARIABLES=============================

running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
handsOriginalResolution = pygame.image.load('Draws/tiny .png')
# tinyHands = pygame.transform.scale(handsOriginalResolution,(380, 161))
# (x,y,w,h) represents a rectangle with top left point at (x,y), with width w and height h.
test = pygame.image.load('Draws/SampleTest.png')
rock = pygame.transform.chop(handsOriginalResolution, (130, 0, 300, 0))
scissors = chop_twice(handsOriginalResolution, (0, 0, 100, 0), (130, 0, 450, 0))
paper = pygame.transform.chop(handsOriginalResolution, (0, 0, 220, 0))
# black = pygame.transform.chop(test,(0,0,250,0))
# =============================================IMPORTANT VARIABLES=============================
# ===================================================GAME LOOP=================================

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((10, 200, 3))
    generate_interface()
    # draw_hands(200, 450)
    pygame.display.update()
