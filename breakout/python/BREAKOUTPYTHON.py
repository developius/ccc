import pygame, sys
from pygame.locals import *

pygame.init()

BALLVSPEED=3;
BALLHSPEED=3;
SPEED=3;
BALLX=325;
BALLY=300;

PADDLEX=0;
PADDLESIZE=0;

LEVEL=0;
MAXLEVEL=3;
LIVES=3;
BLOCKSLEFT=0;
GAMEMODE=0;

SCORE=0;
TOPSCORE=0;

BLACK = (0,0,0)
WHITE =(255,255,255)
BLUE = (125, 125, 200)
RED = (255, 0, 0)
ORANGE = (255, 125, 0)
YELLOW = (255, 255, 0)
LGREEN = (0, 255, 125)
LBLUE = (0, 255,255)
DBLUE = (0,0,255)
PINK = (255,0,255)

LEVELGRID = [

#LEVEL 1
[
[99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
[98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
[97, 97, 97, 97, 97, 97, 97, 97, 97, 97],
[96, 96, 96, 96, 96, 96, 96, 96, 96, 96],
[95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
[94, 94, 94, 94, 94, 94, 94, 94, 94, 94],
[93, 93, 93, 93, 93, 93, 93, 93, 93, 93],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
],

#LEVEL 2
[
[99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
[98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
[97, 97, 97, 97, 97, 97, 97, 97, 97, 97],
[96, 96, 96, 96, 96, 96, 96, 96, 96, 96],
[95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
[94, 94, 94, 94, 94, 94, 94, 94, 94, 94],
[93, 93, 93, 93, 93, 93, 93, 93, 93, 93],
[99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
[99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
[99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
],

#LEVEL 3
[
[99, 98, 97, 96, 95, 95, 96, 97, 98, 99],
[99, 98, 97, 96, 95, 95, 96, 97, 98, 99],
[99, 98, 97, 96, 95, 95, 96, 97, 98, 99],
[99, 98, 97, 96, 95, 95, 96, 97, 98, 99],
[99, 98, 97, 96, 95, 95, 96, 97, 98, 99],
[99, 98, 97, 96,  0,  0, 96, 97, 98, 99],
[99, 98, 97,  0,  0,  0,  0, 97, 98, 99],
[99, 98,  0,  0,  0,  0,  0,  0, 98, 99],
[99,  0,  0,  0,  0,  0,  0,  0,  0, 99],
[90,  0,  0,  0,  0,  0,  0,  0,  0, 90],
],

];


SCREENGRID = [

#BLANKSCREEN
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
];

DISPLAYSURFACE = pyagame.display.set_mode((320,256))
pygame.display.set_caption(‘BREAK OUT’)



def setup():
   for y in range (0,10):
            for x in range (0,10):
                  SCREENGRID[y][x]==SCREENGRID[LEVEL][y][x]
   return

setup();



while True:
      #MAIN GAME LOOP
      DISPLAYSURFACE.fill(BLACK)
      
      if GAMEMODE==0:
      	#TITLESCREEN
      	
      	
      if GAMEMODE==1:
      	#MAINGAME
      	makescreen();
      	check();
      	
      	if (BLOCKSLEFT==0):
            LEVEL++

            if (LEVEL==MAXLEVEL):
            	LEVEL=0;
            
            BALLX=325
            BALLY=300

            for y in range (0,10):
            	for x in range (0,10):
                    SCREENGRID[y][x]==SCREENGRID[LEVEL][y][x]
            
        

        # CHECK LIVES
        if (LIVES==0):
        	GAMEMODE=0
        
            if (SCORE>TOPSCORE):
                TOPSCORE=SCORE

            LIVES=3
            SCORE=0
      
      pygame.display.update()	
      
      
      
      
def makescreen():
   
   
    DISPLAYSURFACE.fill(BLACK)
    

    #DRAW BORDERS
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (325,20,650,40), 0)
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (12,250,25,500), 0)
    pygame.draw.rect(DISPLAYSURFACE, BLUE, (638,250,25,500), 0)

    #DRAW BALL
    pygame.draw.circle(DISPLAYSURFACE, WHITE, (BALLX,BALLY), 10, 0)
    BALLX=BALLX+BALLHSPEED
    BALLY=BALLY+BALLVSPEED
   
   
    #DRAW AND COUNT BLOCKS
    BLOCKSLEFT=0
    for y in range (0,10):
            	for x in range (0,10): 

            if (SCREENGRID [y][x]==99):
                pygame.draw.rect(DISPLAYSURFACE, RED, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==98): 
                pygame.draw.rect(DISPLAYSURFACE, ORANGE, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==97): 
                pygame.draw.rect(DISPLAYSURFACE, YELLOW, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==96): 
                pygame.draw.rect(DISPLAYSURFACE, LGREEN, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==95): 
                pygame.draw.rect(DISPLAYSURFACE, LBLUE (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==94): 
                pygame.draw.rect(DISPLAYSURFACE, DBLUE, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==93): 
                pygame.draw.rect(DISPLAYSURFACE, PINK, (x*60+55, y*20+75, 60, 20), 0)
            
            if (SCREENGRID [y][x]==90): 
                pygame.draw.rect(DISPLAYSURFACE, WHITE, (x*60+55, y*20+75, 60, 20), 0)
            

            if (SCREENGRID [y][x]!=0):
                BLOCKSLEFT++;

   
    pos = pygame.mouse.get_pos()
    PADDLEX=pos[0]
   
   
    if (PADDLEX>55+PADDLESIZE && PADDLEX<595-PADDLESIZE):
        pygame.draw.rect(DISPLAYSURFACE, WHITE, (PADDLEX,480,60+(PADDLESIZE*2),20), 0)
   
    #DRAW PLAYER BUT PREVENT OFF LEFT SIDE
    if (PADDLEX<55+PADDLESIZE):
    	pygame.draw.rect(DISPLAYSURFACE, WHITE, (PADDLEX,480,60+(PADDLESIZE*2),20), 0)

    #DRAW PLAYER BUT PREVENT OFF RIGHT SIDE
    if (PADDLEX>595-PADDLESIZE): 
        pygame.draw.rect(DISPLAYSURFACE, WHITE, (PADDLEX,480,60+(PADDLESIZE*2),20), 0)
   
    return
   
   
   
def check():
   #AGAINST PADDLE
    if (BALLY>470 && BALLX > PADDLEX-30-PADDLESIZE && BALLX < PADDLEX+30+PADDLESIZE):
        if (BALLVSPEED>0): 
            BALLVSPEED=-SPEED


    #OUT OF BOUNDS
    if (BALLY>500):
        LIVES--
        delay(100)
        BALLX=325
        BALLY=300
    

    #AGAINST CEILING
    if (BALLY<45): 
        if (BALLVSPEED<0): 
            BALLVSPEED=SPEED
        
    

    #AGAINST RIGHT WALL
    if (BALLX>620): 
        if (BALLHSPEED>0):
            BALLHSPEED=-SPEED
        
    

    #AGAINST LEFT WALL
    if (BALLX<30): 
        if (BALLHSPEED<0): 
            BALLHSPEED=SPEED
        
    
    #AGAINST BLOCKS
    for y in range (0,10):
            	for x in range (0,10): 

            if (SCREENGRID [y][x]!=0 && BALLX > x*60+25 && BALLX < x*60+85
            && BALLY > y*20+75-10 && BALLY < y*20+75+10):

                if (SCREENGRID [y][x]==99): 
                    SCORE=SCORE+350;
                elif (SCREENGRID [y][x]==98): 
                    SCORE=SCORE+300;
                elif (SCREENGRID [y][x]==97): 
                    SCORE=SCORE+250;
                elif (SCREENGRID [y][x]==96): 
                    SCORE=SCORE+200;
                elif (SCREENGRID [y][x]==95): 
                    SCORE=SCORE+150;
                elif (SCREENGRID [y][x]==94): 
                    SCORE=SCORE+100;
                elif (SCREENGRID [y][x]==93): 
                    SCORE=SCORE+50;
                elif (SCREENGRID [y][x]==90): 
                    SCORE=SCORE+1000;
                

                SCREENGRID [y][x]=0:
                if (BALLVSPEED>0) 
                    BALLVSPEED=-SPEED
                elif (BALLVSPEED<0) :
                    BALLVSPEED=SPEED
                
            
        
    
   
   
   
   return

