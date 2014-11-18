int speakerOut = 8;
int noteLength[ ] =
{
500, 500, 250, 250, 250, 250, 500, 500,
500, 500, 250, 250, 250, 250, 500, 500,
500, 500, 250, 250, 250, 250, 500, 500,
250, 250, 500, 500, 500, 1000,
500, 500, 500, 500, 1000,
500, 500, 500, 500, 1000,
500, 500, 500, 500, 500, 500,
250, 250, 500, 500, 500, 1000
};

int notes[ ] =
{
262, 349, 349, 392, 349, 330, 294, 233,
294, 392, 392, 440, 392, 349, 330, 262,
262, 440, 440, 466, 440, 392, 349, 294,
262, 262, 294, 392, 330, 349,
262, 349, 349, 349, 330,
330, 349, 330, 294, 262,
262, 440, 392, 349, 523, 262,
262, 262, 294, 392, 330, 349
};

void setup()
{
    //This code is run once at the start of the program
    pinMode(speakerOut, OUTPUT);

    for (int i=0;i<52;i++)
    {
        tone(speakerOut, notes[i]);
        delay(noteLength[i]);
        noTone(speakerOut);

    }

}

void loop()
{
    //This code is run repeatedly until the program terminates.

}
