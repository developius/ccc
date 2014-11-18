void setup()
{
    //CODE IN HERE IS RUN ONCE AT THE BEGINNING
    size(650,500);
    background(0,0,0);
    rectMode(CENTER);
}

void draw()
{
    //CODE IN HERE IS RUN REPEATEDLY UNTIL THE PROGRAM STOPS
    float r=random(255);
    float g=random(255);
    float b=random(255);

    float s=random(50,400);
    float s2=random(50,400);

    float x=random(650);
    float y=random(500);

    float o=random(255);

    float t=random(2);

    fill(r,g,b,o);
    if (t<1){rect(x,y,s,s2);}
    if (t>1){ellipse(x,y,s,s2);}

    //FADE TO BLACK
    fill(0,0,0,5);
    rect(325,250,650,500);
}
