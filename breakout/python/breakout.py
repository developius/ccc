import pygame
import sys
import time
from pygame.locals import *
import pygame.mouse

pygame.init()

font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 20)


BALLVSPEED = 2
BALLHSPEED = 2
SPEED = 2
BALLX = 162
BALLY = 150

PADDLEX = 0
PADDLESIZE = 0

LEVEL = 0
MAXLEVEL = 3
LIVES = 3
BLOCKSLEFT = 0
GAMEMODE = 0

SCORE = 0
TOPSCORE = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (125, 125, 200)
RED = (255, 0, 0)
ORANGE = (255, 125, 0)
YELLOW = (255, 255, 0)
LGREEN = (0, 255, 125)
LBLUE = (0, 255, 255)
DBLUE = (0, 0, 255)
PINK = (255, 0, 255)

clock = pygame.time.Clock()

LEVELGRID = [

    # LEVEL 1
    [
        [99, 99, 99, 99, 99, 99, 99, 99, 99, 0],
        [98, 98, 98, 98, 98, 98, 98, 98, 98, 0],
        [97, 97, 97, 97, 97, 97, 97, 97, 97, 0],
        [96, 96, 96, 96, 96, 96, 96, 96, 96, 0],
        [95, 95, 95, 95, 95, 95, 95, 95, 95, 0],
        [94, 94, 94, 94, 94, 94, 94, 94, 94, 0],
        [93, 93, 93, 93, 93, 93, 93, 93, 93, 0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ],

    # LEVEL 2
    [
        [99, 99, 99, 99, 99, 99, 99, 99, 99, 0],
        [98, 98, 98, 98, 98, 98, 98, 98, 98, 0],
        [97, 97, 97, 97, 97, 97, 97, 97, 97, 0],
        [96, 96, 96, 96, 96, 96, 96, 96, 96, 0],
        [95, 95, 95, 95, 95, 95, 95, 95, 95, 0],
        [94, 94, 94, 94, 94, 94, 94, 94, 94, 0],
        [93, 93, 93, 93, 93, 93, 93, 93, 93, 0],
        [99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
        [99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
        [99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
    ],

    # LEVEL 3
    [
        [99, 98, 97, 96, 95, 96, 97, 98, 99, 0],
        [99, 98, 97, 96, 95, 96, 97, 98, 99, 0],
        [99, 98, 97, 96, 95, 96, 97, 98, 99, 0],
        [99, 98, 97, 96, 95, 96, 97, 98, 99, 0],
        [99, 98, 97, 96, 0, 96, 97, 98, 99, 0],
        [99, 98, 97, 0,  0, 0, 97, 98, 99, 0],
        [99, 98, 0,  0,  0,  0, 0, 98, 99, 0],
        [99, 0,  0,  0,  0,  0,  0, 0, 99, 0],
        [90,  0,  0,  0,  0,  0,  0,  0, 90, 0],
        [0,  0,  0,  0,  0,  0,  0,  0, 0, 0],
    ],

]


SCREENGRID = [

    # BLANKSCREEN
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
]

DISPLAYSURFACE = pygame.display.set_mode((325, 250))
pygame.display.set_caption('       BREAK OUT')


def setup():
    global LIVES
    global SCORE
    global LEVEL
    global GAMEMODE

    for y in range(0, 9):
        for x in range(0, 9):
            SCREENGRID[y][x] = LEVELGRID[LEVEL][y][x]
    LIVES = 3
    SCORE = 0
    LEVEL = 0
    GAMEMODE = 0

    return

setup()


def makescreen():

    DISPLAYSURFACE.fill(BLACK)

    # DRAW BORDERS
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (0, 0, 325, 20), 0)
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (0, 0, 26, 250), 0)
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (299, 0, 26, 250), 0)

    # DRAW BALL
    global BALLX
    global BALLY
    pygame.draw.circle(DISPLAYSURFACE, WHITE, (BALLX, BALLY), 3, 0)
    BALLX = BALLX + BALLHSPEED
    BALLY = BALLY + BALLVSPEED

    # DRAW AND COUNT BLOCKS
    global BLOCKSLEFT
    BLOCKSLEFT = 0
    for y in range(0, 10):
        for x in range(0, 9):

            if (SCREENGRID[y][x] == 99):
                pygame.draw.rect(
                    DISPLAYSURFACE, RED, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 98):
                pygame.draw.rect(
                    DISPLAYSURFACE, ORANGE, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 97):
                pygame.draw.rect(
                    DISPLAYSURFACE, YELLOW, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 96):
                pygame.draw.rect(
                    DISPLAYSURFACE, LGREEN, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 95):
                pygame.draw.rect(
                    DISPLAYSURFACE, LBLUE, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 94):
                pygame.draw.rect(
                    DISPLAYSURFACE, DBLUE, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 93):
                pygame.draw.rect(
                    DISPLAYSURFACE, PINK, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] == 90):
                pygame.draw.rect(
                    DISPLAYSURFACE, WHITE, (x * 30 + 27, y * 10 + 35, 29, 9), 0)

            if (SCREENGRID[y][x] != 0):
                BLOCKSLEFT = BLOCKSLEFT + 1

    global PADDLEX
    global PADDLESIZE

    # DRAW PLAYER BUT PREVENT OFF LEFT SIDE
    if (PADDLEX < 25 + PADDLESIZE):
        PADDLEX = 25

    # DRAW PLAYER BUT PREVENT OFF RIGHT SIDE
    if (PADDLEX > 269 - PADDLESIZE):
        PADDLEX = 269

    if (PADDLEX > 24 + PADDLESIZE and PADDLEX < 270 - PADDLESIZE):
        pygame.draw.rect(
            DISPLAYSURFACE, WHITE, (PADDLEX, 240, 30 + (PADDLESIZE * 2), 10), 0)

    return


def check():
    global BALLX
    global BALLY
    global PADDLEX
    global PADDLESIZE
    global SPEED
    global LIVES
    global BALLVSPEED
    global BALLHSPEED
    global SCORE

    # AGAINST PADDLE
    if (BALLY > 235 and (BALLX > PADDLEX - 25 and BALLX < PADDLEX + 25)):
        if (BALLVSPEED > 0):
            BALLVSPEED = -SPEED

    # OUT OF BOUNDS
    if (BALLY > 260):
        LIVES = LIVES - 1
        time.sleep(1)
        BALLX = 162
        BALLY = 150

    # AGAINST CEILING
    if (BALLY < 22):
        if (BALLVSPEED < 0):
            BALLVSPEED = SPEED

    # AGAINST RIGHT WALL
    if (BALLX > 297):
        if (BALLHSPEED > 0):
            BALLHSPEED = -SPEED

    # AGAINST LEFT WALL
    if (BALLX < 28):
        if (BALLHSPEED < 0):
            BALLHSPEED = SPEED

    # AGAINST BLOCKS
    for y in range(0, 10):
        for x in range(0, 9):

            if (SCREENGRID[y][x] != 0 and BALLX > x * 30 + 27 and BALLX < x * 30 + 57
                    and BALLY > y * 10 + 35 and BALLY < y * 10 + 35 + 10):

                if (SCREENGRID[y][x] == 99):
                    SCORE = SCORE + 350
                elif (SCREENGRID[y][x] == 98):
                    SCORE = SCORE + 300
                elif (SCREENGRID[y][x] == 97):
                    SCORE = SCORE + 250
                elif (SCREENGRID[y][x] == 96):
                    SCORE = SCORE + 200
                elif (SCREENGRID[y][x] == 95):
                    SCORE = SCORE + 150
                elif (SCREENGRID[y][x] == 94):
                    SCORE = SCORE + 100
                elif (SCREENGRID[y][x] == 93):
                    SCORE = SCORE + 50
                elif (SCREENGRID[y][x] == 90):
                    SCORE = SCORE + 1000

                SCREENGRID[y][x] = 0
                if (BALLVSPEED > 0):
                    BALLVSPEED = -SPEED
                elif (BALLVSPEED < 0):
                    BALLVSPEED = SPEED

    return


running = True
while running:

    # MAIN GAME LOOP
    DISPLAYSURFACE.fill(BLACK)

    clock.tick(60)

    if (GAMEMODE == 0):
        # TITLESCREEN
        text2 = font2.render(
            "TOP SCORE " + str(TOPSCORE), True, (255, 255, 255))
        DISPLAYSURFACE.blit(text2, (12, 3))

        text = font.render("BREAK OUT", True, (255, 255, 255))
        DISPLAYSURFACE.blit(text, (60, 90))

        text3 = font2.render("PRESS SPACE TO START", True, (255, 255, 255))
        DISPLAYSURFACE.blit(text3, (80, 180))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE):
                    GAMEMODE = 1

                if (event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

    if (GAMEMODE == 1):
        # MAINGAME
        makescreen()

        text3 = font2.render("SCORE " + str(SCORE), True, (255, 255, 255))
        DISPLAYSURFACE.blit(text3, (25, 3))

        text4 = font2.render("LIVES " + str(LIVES), True, (255, 255, 255))
        DISPLAYSURFACE.blit(text4, (140, 3))

        text5 = font2.render("LEVEL " + str(LEVEL + 1), True, (255, 255, 255))
        DISPLAYSURFACE.blit(text5, (245, 3))

        check()

        # CHANGELEVEL
        if (BLOCKSLEFT == 0):
            LEVEL = LEVEL + 1

            if (LEVEL == MAXLEVEL):
                LEVEL = 0

            BALLX = 162
            BALLY = 150

            for y in range(0, 10):
                for x in range(0, 9):
                    SCREENGRID[y][x] = 0

            for y in range(0, 10):
                for x in range(0, 9):
                    SCREENGRID[y][x] = LEVELGRID[LEVEL][y][x]

        # CHECK LIVES
        if (LIVES == 0):
            GAMEMODE = 0

            if (SCORE > TOPSCORE):
                TOPSCORE = SCORE

            setup()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pos = pygame.mouse.get_pos()
            PADDLEX = pos[0] - 15

            if event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

        # HACK
        # PADDLEX=BALLX-15

    pygame.display.update()
