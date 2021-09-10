import pygame
import random

#=========================== Classes and methods===============
#This class is in charge of set hitbox to the screen interface
class Box():

    def __init__(self, xStart, xEnd, yStart, yEnd):
        self._xStart = xStart
        self._xEnd = xEnd
        self._yStart = yStart
        self._yEnd = yEnd
        #self.square = (self._xStart, self._xEnd, self._yStart, self._yEnd)
    def check_limits(self, x, y):
        if self._xStart <= x <= self._xEnd and self._yStart <= y <= self._yEnd:
            return True

# JUST FOR TESTING PROPOSES. It does what it says it blit the different hands in to the game.
#   def draw_hands(x, y):
#   screen.blit(handsOriginalResolution, (x, y))
#   screen.blit(black, (x, y))
#   screen.blit(paper, (x, y))
#   screen.blit(rock, (x, y))
#   pass
# =============================================METHODS==========================================
# ==============Image related Methods==============#

# This special method chop an image two times to create another. In this case i used for take
# A scissors
def chop_twice(surface, tuple1, tuple2):
    subsurface = pygame.transform.chop(surface, tuple1)
    sub_subsurface = pygame.transform.chop(subsurface, tuple2)
    return sub_subsurface


# ==============Image related Methods==============#
# ==============Action Related Methods=============#



# ==============Hand related Methods==============#
# This method create blit a hand depending on what hand you chose, also you need to specify the
# direction of the hand, by default it set as flipped but you should specify what you want
def draw_hands(hand, x, y, flipped=True):
    # Normal Hands
    if hand == "rock" and False == flipped:
        screen.blit(rock, (x, y))
    elif hand == "paper" and flipped == False:
        screen.blit(paper, (x, y))
    elif hand == "scissors" and flipped == False:
        screen.blit(scissors, (x, y))
    # Flipped hands
    if hand == "rock" and flipped == True:
        screen.blit(rockF, (x, y))
    elif hand == "paper" and flipped == True:
        screen.blit(paperF, (x, y))
    elif hand == "scissors" and flipped == True:
        screen.blit(scissorsF, (x, y))


# This method generate the main interface
def generate_interface():
    draw_hands("rock", 200, 400, False)
    draw_hands("paper", 300, 400, False)
    draw_hands("scissors", 500, 400, False)
    # draw_hands("scissors", 300, 50, True)


# =============================================IMPORTANT VARIABLES=============================

running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
handsOriginalResolution = pygame.image.load('Draws/tiny .png')
# tinyHands = pygame.transform.scale(handsOriginalResolution,(380, 161))
# (x,y,w,h) represents a rectangle with top left point at (x,y), with width w and height h.
test = pygame.image.load('Draws/SampleTest.png')

# Normal Hands
rock = pygame.transform.chop(handsOriginalResolution, (130, 0, 300, 0))
scissors = chop_twice(handsOriginalResolution, (0, 0, 100, 0), (130, 0, 450, 0))
paper = pygame.transform.chop(handsOriginalResolution, (0, 0, 220, 0))

# Flipped hands
rockF = pygame.transform.flip(rock, False, True)
scissorsF = pygame.transform.flip(scissors, False, True)
paperF = pygame.transform.flip(paper, False, True)
# Important objects
# Hitboxes
handHitbox = Box(312, 467, 385, 541)

# black = pygame.transform.chop(test,(0,0,250,0))
# =============================================IMPORTANT VARIABLES=============================
# ===================================================GAME LOOP=================================

while running:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and handHitbox.check_limits(x, y):
            print("yea you click it")



    screen.fill((10, 200, 3))
    generate_interface()
    # draw_hands(200, 450)
    pygame.display.update()
