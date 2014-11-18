# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
#SETUP VARIABLES
GOODX=0
GOODY=0
GREEN = (0,0,255)
BLUE=(0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)

SCREENGRID = [
[99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
[99,   1, 99, 97,   0, 99,   0,   0,   0, 99],
[99,   0, 99, 99,   0,   0,   0, 99,   0, 99],
[99,   0, 99, 99, 99, 99, 99, 99,   0, 99],
[99,   0,   0, 99,   0,   0,   0, 99,   0, 99],
[99, 99,   0, 99,   0, 99,   0, 99,   0, 99],
[99, 99,   0,   0,   0, 99,   0,   0,   0, 99],
[99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
];

DISPLAYSURFACE = pygame.display.set_mode((320,256))
pygame.display.set_caption('MAZE GAME')

#FIND HERO LOCATION
for y in range (0,8):
	for x in range (0,10):
		if SCREENGRID[y][x]==1:
			GOODX=x
			GOODY=y

while True:
	#MAIN GAME LOOP
	DISPLAYSURFACE.fill(WHITE)

	#DRAW MAZE
	for y in range (0,8):
		for x in range (0,10):
			if SCREENGRID[y][x]==99:
				pygame.draw.rect(DISPLAYSURFACE,GREEN, (32*x,32*y,31,31))
			if SCREENGRID[y][x]==97:
				pygame.draw.rect(DISPLAYSURFACE,BLUE, (32*x,32*y,31,31))

	#DRAW GOODGUY
	pygame.draw.rect(DISPLAYSURFACE,RED,(32*GOODX,32*GOODY,31,31))


	if SCREENGRID[GOODY][GOODX]==97:
		DISPLAYSURFACE.fill(WHITE)
		for y in range (0,8):
			for x in range (0,10):
				if SCREENGRID[y][x]==1:
					GOODX=x
					GOODY=y

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if (event.key == K_LEFT) and SCREENGRID[GOODY][GOODX-1]!=99: GOODX=GOODX-1
			if (event.key == K_RIGHT) and SCREENGRID[GOODY][GOODX+1]!=99: GOODX=GOODX+1
			if (event.key == K_DOWN) and SCREENGRID[GOODY+1][GOODX]!=99: GOODY=GOODY+1
			if (event.key == K_UP) and SCREENGRID[GOODY-1][GOODX]!=99: GOODY=GOODY-1
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
