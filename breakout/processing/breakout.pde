PFont font;

int BALLVSPEED=3;
int BALLHSPEED=3;
int BALLX=325;
int BALLY=300;

int PADDLEX=0;
int PADDLESIZE=0;

int LEVEL=0;
int MAXLEVEL=3;
int LIVES=3;
int BLOCKSLEFT=0;
int GAMEMODE=0;

int SCORE=0;
int TOPSCORE=0;

void setup()
{
    size (650, 500);
    background(0, 0, 0);
    rectMode(CENTER);
    noCursor();

    font = loadFont("ArialMT-100.vlw"); }

void draw()
{
    //TITLE SCREEN
    if (GAMEMODE==0) {

        background(0);
        textFont(font, 20);
        text("TOP SCORE: "+TOPSCORE, 25, 30);

        textFont(font, 100);
        text("BREAK OUT", 40, 200);

        textFont(font, 20);
        text("PRESS SPACE TO START", 205, 400);

        if (keyPressed) {
            if (key == ' ' ) {
                GAMEMODE=1;
                for (int y = 0; y < 10; y++) {
                    for (int x = 0; x < 10; x++) {
                        SCREENGRID [y][x]=LEVELGRID [LEVEL] [y][x];
                    }
                }
            }
        }
    }

    //GAME SCREEN
    if (GAMEMODE==1) {
        makescreen();
        check();

        if (BLOCKSLEFT==0) {
            LEVEL++;

            if (LEVEL==MAXLEVEL){LEVEL=0;}
            BALLX=325;
            BALLY=300;

            for (int y = 0; y < 10; y++) {
                for (int x = 0; x < 10; x++) {
                    SCREENGRID [y][x]=LEVELGRID [LEVEL] [y][x];
                }
            }

        }

        // CHECK LIVES
        if (LIVES==0) {
        GAMEMODE=0;
            if (SCORE>TOPSCORE) {
                TOPSCORE=SCORE;
            }
            LIVES=3;
            SCORE=0;
        }

    }

}

void makescreen()
{
    background(0);
    noStroke();

    //DRAW BORDERS
    fill(125, 125, 200);
    rect(325, 20, 650, 40);
    rect(12, 250, 25, 500);
    rect(638, 250, 25, 500);

    //DRAW BALL
    fill(255);
    ellipse(BALLX, BALLY, 10, 10);
    BALLX=BALLX+BALLHSPEED;
    BALLY=BALLY+BALLVSPEED;

    //DRAW SCORE
    fill(0);
    rect(325, 22, 600, 20);
    fill(255);
    textFont(font, 20);
    text("SCORE: "+SCORE, 25, 30);
    text("LIVES: "+LIVES, 290, 30);
    text("LEVEL: "+(LEVEL+1), 530, 30);

    //DRAW AND COUNT BLOCKS
    stroke(0);
    for (int y = 0; y < 10; y++) {
        for (int x = 0; x < 10; x++) {

            if (SCREENGRID [y][x]==99) {
                fill(255, 0, 0);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==98) {
                fill(255, 125, 0);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==97) {
                fill(255, 255, 0);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==96) {
                fill(0, 255, 125);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==95) {
                fill(0, 255, 255);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==94) {
                fill(0, 0, 255);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==93) {
                fill(255, 0, 255);
                rect(x*60+55, y*20+75, 60, 20);
            }
            if (SCREENGRID [y][x]==90) {
                fill(255, 255, 255);
                rect(x*60+55, y*20+75, 60, 20);
            }

            if (SCREENGRID [y][x]!=0) {
                BLOCKSLEFT++;
            }
        }
    }

    PADDLEX=mouseX;

    //DRAW PLAYER NORMALLY
    fill(255);
    if (PADDLEX>55+PADDLESIZE && PADDLEX<595-PADDLESIZE) {
        rect (PADDLEX, 480, 60+(PADDLESIZE*2), 20,10);
    }

    //DRAW PLAYER BUT PREVENT OFF LEFT SIDE
    if (PADDLEX<55+PADDLESIZE) {
        rect (55+PADDLESIZE, 480, 60+(PADDLESIZE*2), 20,10);
    }

    //DRAW PLAYER BUT PREVENT OFF RIGHT SIDE
    if (PADDLEX>595-PADDLESIZE) {
        rect (595-PADDLESIZE, 480, 60+(PADDLESIZE*2), 20,10);
    }
}

void check()
{

    //AGAINST PADDLE
    if (BALLY>470 && BALLX > PADDLEX-30-PADDLESIZE && BALLX < PADDLEX+30+PADDLESIZE)
        {
        if (BALLVSPEED==3) {
            BALLVSPEED=-3;
        }
    }

    //OUT OF BOUNDS
    if (BALLY>500) {
        LIVES--;
        delay(100);
        BALLX=325;
        BALLY=300;
    }

    //AGAINST CEILING
    if (BALLY<45) {
        if (BALLVSPEED==-3) {
            BALLVSPEED=3;
        }
    }

    //AGAINST RIGHT WALL
    if (BALLX>620) {
        if (BALLHSPEED==3) {
            BALLHSPEED=-3;
        }
    }

    //AGAINST LEFT WALL
    if (BALLX<30) {
        if (BALLHSPEED==-3) {
            BALLHSPEED=3;
        }
    }

    //AGAINST BLOCKS
    for (int y = 0; y < 10; y++) {
        for (int x = 0; x < 10; x++) {

            if (SCREENGRID [y][x]!=0 && BALLX > x*60+25 && BALLX < x*60+85
            && BALLY > y*20+75-10 && BALLY < y*20+75+10) {

                if (SCREENGRID [y][x]==99) {
                    SCORE=SCORE+350;
                } else if (SCREENGRID [y][x]==98) {
                    SCORE=SCORE+300;
                } else if (SCREENGRID [y][x]==97) {
                    SCORE=SCORE+250;
                } else if (SCREENGRID [y][x]==96) {
                    SCORE=SCORE+200;
                } else if (SCREENGRID [y][x]==95) {
                    SCORE=SCORE+150;
                } else if (SCREENGRID [y][x]==94) {
                    SCORE=SCORE+100;
                } else if (SCREENGRID [y][x]==93) {
                    SCORE=SCORE+50;
                } else if (SCREENGRID [y][x]==90) {
                    SCORE=SCORE+1000;
                }

                SCREENGRID [y][x]=0;
                if (BALLVSPEED==3) {
                    BALLVSPEED=-3;
                } else if (BALLVSPEED==-3) {
                    BALLVSPEED=3;
                }
            }
        }
    }

}
