import pygame
import random


# =========================== Classes and methods===============
# This class is in charge of set hitbox to the screen interface
class Box:
    def __init__(self, xStart, xEnd, yStart, yEnd):
        self._xStart = xStart
        self._xEnd = xEnd
        self._yStart = yStart
        self._yEnd = yEnd
        # self.square = (self._xStart, self._xEnd, self._yStart, self._yEnd)

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
# Detect the choice of the enemy based on a random action and return the value of the winer pick
def detect(player_pick):
    enemy_pick = random.choice(['rock', 'paper', 'scissors'])
    ##========Rock detection=======##
    # Compare with scissors
    if enemy_pick == 'rock' and player_pick == 'scissors':
        print("You lose")
        return "rock_win_enemy"
        # Enemy will win with rock
    elif enemy_pick == 'scissors' and player_pick == 'rock':
        print("You Win")
        return "scissors_lose_enemy"
        # Enemy will lose with rock

    # Compare with paper

    elif enemy_pick == 'rock' and player_pick == 'paper':
        print("You Win")
        return "rock_lose_enemy"

    elif enemy_pick == 'paper' and player_pick == 'rock':
        print("You lose")
        return "paper_win_enemy"



    # Compare ties
    elif enemy_pick == 'rock' and player_pick == 'rock':
        print("Tie")
        return "rock_tie"
    elif enemy_pick == 'paper' and player_pick == 'paper':
        print("Tie")
        return "paper_tie"
    elif enemy_pick == 'scissors' and player_pick == 'scissors':
        print("Tie")
        return "scissors_tie"


# ==============Hand related Methods==============#
# This method create blit a hand depending on what hand you chose, also you need to specify the
# direction of the hand, by default it set as flipped but you should specify what you want
def draw_hands(hand, x, y, flipped=True):
    # Normal Hands
    if hand == "rock" and flipped == False:
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
def generate_player_interface():
    draw_hands("rock", 200, 400, False)
    draw_hands("paper", 300, 400, False)
    draw_hands("scissors", 500, 400, False)


# Draw the enemy hand based on the result of the detect method.
def draw_enemy_hand(enemy_decision_result):
    x = 300
    y = 0
    if enemy_decision_result == "rock_win_enemy":
        draw_hands("rock", x, y, True)
    elif enemy_decision_result == "rock_lose_enemy":
        draw_hands("rock", x, y, True)

    if enemy_decision_result == "paper_win_enemy":
        draw_hands("paper", x, y, True)
    elif enemy_decision_result == "paper_lose_enemy":
        draw_hands("paper", x, y, True)

    if enemy_decision_result == "scissors_win_enemy":
        draw_hands("scissors", x, y, True)
    elif enemy_decision_result == "scissors_lose_enemy":
        draw_hands("scissors", x, y, True)

    if enemy_decision_result == "scissors_tie":
        draw_hands("scissors", x, y, True)
    elif enemy_decision_result == "rock_tie":
        draw_hands("paper", x, y, True)
    elif enemy_decision_result == "paper_tie":
        draw_hands("paper", x, y, True)


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

# Flipped hands / Enemy hands
rockF = pygame.transform.flip(rock, False, True)
scissorsF = pygame.transform.flip(scissors, False, True)
paperF = pygame.transform.flip(paper, False, True)
# Visible/Invisible Enemy hands
decision = "invisble"

# Important objects
# Hitboxes
paperHitbox = Box(312, 467, 385, 541)
rockHibox = Box(189, 304, 435, 547)
scissorsHitbox = Box(502, 630, 411, 552)
# black = pygame.transform.chop(test,(0,0,250,0))
# =============================================IMPORTANT VARIABLES=============================
# ===================================================GAME LOOP=================================

while running:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and paperHitbox.check_limits(x, y):
            print("yea you click it paper")
            decision = detect("paper")
        if event.type == pygame.MOUSEBUTTONDOWN and rockHibox.check_limits(x, y):
            print("yea you click it rock")
            decision = detect("rock")
        if event.type == pygame.MOUSEBUTTONDOWN and scissorsHitbox.check_limits(x, y):
            print("yea you click it scissors")
            decision = detect("scissors")
    # print(x, y)

    screen.fill((10, 200, 3))
    draw_enemy_hand(decision)
    generate_player_interface()
    # draw_hands(200, 450)
    pygame.display.update()
