
///////////////////////////////////////////////////////////////////////
// Filename: ISRs.c
//
// Synopsis: Interrupt service routine for codec data transmit/receive
//
// Author: Alexander Perr
//
// Project: Time Machine 2
//
// Notes: printf and other functions are commented out but are still left in for further development
///////////////////////////////////////////////////////////////////////

#include "DSP_Config.h" 
#include "Echo.h" 
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
  
// Data is received as 2 16-bit words (left/right) packed into one
// 32-bit word.  The union allows the data to be accessed as a single 
// entity when transferring to and from the serial port, but still be 
// able to manipulate the left and right channels independently.

#define LEFT  0
#define RIGHT 1

#define PI 3.14159265


volatile union 
{
    Uint32 UINT;
    Int16 Channel[2];
} CodecDataIn, CodecDataOut;


//GLOBAL VARIABLES
//**********************************************
//Recording
int serialStore = 0;                  //stores serial value from main to maintain setTimeMachine function call
int recIndex = 0;		      //variable for  recording index pointer
int time = 0;			      //variable for time used for the 4 beat time window when button pressed
int goBack = 0;			      //pointer used to set pointer back into the buffer over a period of time
int bufferEnd = (24000*8);//default to 120 bpm
int fluxCapacitor = 0;		      //playback pointer used to navagate through the buffer 
float xLeft, xRight, yLeft, yRight;
#define BUFFER_LENGTH   1152000       // buffer length in samples
#pragma DATA_SECTION (buffer, "CE0"); // put "buffer" in SDRAM
volatile float buffer[2][BUFFER_LENGTH]; // space for left + right

//Wet Playback
int activeButton = 0;
int playbackIndex = 0;


//Tap Tempo
int sampleCounter = 144000;
int oneBeat = 24000;


void ZeroBuffer()
///////////////////////////////////////////////////////////////////////
// Purpose:   Initial fill of all buffer locations with 0.0
//
// Input:     None
//
// Returns:   Nothing
//
// Calls:     Nothing
//
// Notes:     None
///////////////////////////////////////////////////////////////////////
{
    int i;

    for(i=0; i < BUFFER_LENGTH; i++)
    {
        buffer[LEFT][i] = 0.0;
        buffer[RIGHT][i] = 0.0;  
    }
}

//SET ACTIVE BUTTON
//*******************************
void setActiveButton(int newButtonValue)
{
    activeButton = newButtonValue;
}

//TAP TEMPO
//*********
void tapTempo()
{

    //if sampleCounter is less than maximum beat size (20 samples), set oneBeat to current number of samples
    if (sampleCounter < 144000)
    {

            //1beat
            oneBeat = sampleCounter;

            //printf("%d\n", oneBeat);

            //set buffer size
            bufferEnd = (oneBeat*8);     //changes the buffersize. 8 beats.

     }

     sampleCounter = 0;
}

void shiftTempoUp()
{
    oneBeat = oneBeat - 500;
}

void shiftTempoDown()
{
    oneBeat = oneBeat + 500;
}

//Time used in TimeMachine functions. Set to repeat after 4 beats
//******************************

void Time()
{
    time++;

    if(time == (4*oneBeat))
    {
       //printf("%d\n", time);
       time = 0;
    }

}

//Time Machine Functions
//creates the logic for differential equations
int Step(int passTime)
{
    if(passTime < 0)
    {
        return 0;
    }
    else if(passTime >= 0)
    {
        return oneBeat;
    }
}

int Ramp(int passTime, int passTime2, double passSlope)
{
    int slopeProd = passSlope*passTime2;

    if(passTime >= 0)
    {
        return slopeProd;
    }
    else if(passTime < 0)
    {
        return 0;
    }
}

int Spin(int passTime, int passTime2, int passAmp, double passDecay)
{

    int spinProd = passAmp*exp(passDecay*passTime2);

    //printf("%d\n", spinProd);

    if(passTime >= 0)
    {
        return spinProd;
    }
    else if(passTime < 0)
    {
        return 0;
    }
}

//SET Time Machine
//creates the time signal using the differential equations that changes the playback pointer over the 4 beat time period when pressed
void setTimeMachine(int serialPass)
{

    //serial commands get called here. This section contains differential functions that determine how far back in time to go.

    serialStore = serialPass;
    int OB = oneBeat;
    //printf("%d\n", time);

    setActiveButton(1);

    if(serialStore == 49)                                         //1 BEAT REPEAT
    {
        goBack = 0-Step((time-oneBeat))-Step((time-2*oneBeat))-Step((time-3*oneBeat));
        //printf("%d\n", time);

    }
    else if(serialPass == 50)                                     //1/2 BEAT REPEAT
    {
        goBack = 0-(0.5)*Step((time-(0.5)*oneBeat))-(0.5)*Step((time-1*oneBeat))-(0.5)*Step((time-(1.5)*oneBeat))-(0.5)*Step((time-2*oneBeat))
                -(0.5)*Step((time-(2.5)*oneBeat))-(0.5)*Step((time-(3)*oneBeat))-(0.5)*Step((time-(3.5)*oneBeat));

    }
    else if(serialPass == 51)                                     //1/3 Beat REPEAT
    {
        goBack = 0-(0.3333)*Step((time-(0.3333)*oneBeat))-(0.3333)*Step((time-(0.6666)*oneBeat))-(0.3333)*Step((time-(1)*oneBeat))
                -(0.3333)*Step((time-(1.3333)*oneBeat))-(0.3333)*Step((time-(1.6666)*oneBeat))-(0.3333)*Step((time-(2)*oneBeat))
                -(0.3333)*Step((time-(2.3333)*oneBeat))-(0.3333)*Step((time-(2.6666)*oneBeat))-(0.3333)*Step((time-(3)*oneBeat))
                -(0.3333)*Step((time-(3.3333)*oneBeat))-(0.3333)*Step((time-(3.6666)*oneBeat))-(0.3333)*Step((time-(4)*oneBeat));
    }
    else if(serialPass == 52)                                     //1/4 BEAT REPEAT
    {
      	goBack = 0-(0.25)*Step((time-(0.25)*oneBeat))-(0.25)*Step((time-(0.5)*oneBeat))-(0.25)*Step((time-(0.75)*oneBeat))-(0.25)*Step((time-oneBeat))
                -(0.25)*Step((time-(1.25)*oneBeat))-(0.25)*Step((time-(1.5)*oneBeat))-(0.25)*Step((time-(1.75)*oneBeat))-(0.25)*Step((time-(2)*oneBeat))
                -(0.25)*Step((time-(2.25)*oneBeat))-(0.25)*Step((time-(2.5)*oneBeat))-(0.25)*Step((time-(2.75)*oneBeat))-(0.25)*Step((time-(3)*oneBeat))
                -(0.25)*Step((time-(3.25)*oneBeat))-(0.25)*Step((time-(3.5)*oneBeat))-(0.25)*Step((time-(3.75)*oneBeat))-(0.25)*Step((time-(4)*oneBeat));

    }
    else if(serialPass == 53)                                      //Reverse
    {
       goBack = Ramp(time, time, -2);
    }
    else if(serialPass == 54)                                       //1/2 Speed
    {
       goBack = Ramp(time, time, -0.5);
    }
    else if(serialPass == 55)                                       //2X Speed
    {
       goBack = Ramp(time, (time-4*oneBeat), 1);
    }
    else if(serialPass ==56)                                        //Slow Triplet
    {
       goBack = Ramp(time, time, -0.25)+Ramp((time-oneBeat), time, 0.25)+Ramp((time-oneBeat),(time-oneBeat), -0.25)
                +Ramp((time-2*oneBeat),(time-oneBeat), 0.25)+Ramp((time-2*oneBeat),(time-2*oneBeat), -0.25)+Ramp((time-3*oneBeat),(time-2*oneBeat), 0.25)+Ramp((time-3*oneBeat),(time-3*oneBeat), -0.25);
    }
    else if(serialPass == 57)                                      //BackSpin Start
    {
       goBack = -4*oneBeat + Spin(time, time, 4*oneBeat, -0.00005);
    }
    else if(serialPass == 58)                                      //Vinyl Off
    {
       goBack = oneBeat + Spin(time, time, -oneBeat, 0.00001);

    }
    else if(serialPass == 59)                                       //Stutter 1
    {
       goBack = Ramp((time-1.5*oneBeat),(time-1.5*oneBeat),-2) + Ramp((time-2*oneBeat),(time-1.5*oneBeat),2)-(0.5)*Step((time-2.5*oneBeat))
                +(0.5)*Step((time-3*oneBeat))-(0.5)*Step((time-3.5*oneBeat));
    }
    else if(serialPass == 60)                                      //Stutter 2
    {
       goBack = -(0.25)*Step((time-0.25*OB))-(0.25)*Step((time-0.5*OB))+(0.5)*Step((time-OB))-(0.25)*Step((time-1.25*OB))-(0.25)*Step((time-1.5*OB))+(0.5)*Step((time-2*OB))-(0.25)*Step((time-2.25*OB))-(0.25)*Step((time-2.5*OB))+(0.5)*Step((time-3*OB))-(0.25)*Step((time-3.25*OB))-(0.25)*Step((time-3.5*OB));
    }
    else if(serialPass == 61)                                      //Stutter 3
    {
       goBack = -(0.25)*Step((time-1.5*OB))+(0.25)*Step((time-2.5*OB))-(0.25)*Step((time-3*OB))-(0.25)*Step((time-3.5*OB));
    }
    else if(serialPass == 62)                                      //Stutter 4
    {
       goBack = -(0.5)*Step((time-0.5*OB))+(0.5)*Step((time-OB))-(0.5)*Step((time-1.5*OB))-(0.5)*Step((time-1.75*OB))+(0.5)*Step((time-2.25*OB))+(0.25)*Step((time-3*OB))-(0.5)*Step((time-3.5*OB))-(1.5)*Step((time-3.75*OB));
    }
    else if(serialPass == 63)                                      //Shuffle
    {
       goBack = 0-3*Step(time)+(2)*Step((time-OB))-Step((time-2*OB))+(2)*Step((time-3*OB));
    }
    else if(serialPass == 64)                                      //Shuffle 2
    {
       goBack = -Step(time)+Step((time-OB))-(2)*Step((time-2*OB))+Step((time-3*OB));
    }
    else if(serialPass == 65)                                      //Swing
    {
        goBack = -Step((time-OB))+(0.25)*Step((time-1.25*OB))-(0.25)*Step((time-2.25*OB))+(0.5)*Step((time-2.5*OB))
                +(0.5)*Step((time-3*OB));
    }
    else if(serialPass == 66)                                  //Basic
    {
        goBack = -(0.5)*Step((time-0.5*OB))+(0.5)*Step((time-OB))+Ramp((time-2*OB),(time-2*OB),-0.25)
                +Ramp((time-3*OB),(time-2*OB),0.25);
    }
    else if(serialPass == 67)                                   //Complex
    {
        goBack = -Step((time-OB))+(0.25)*Step((time-1.25*OB))+(0.5)*Step((time-(1.5)*OB))-0.5*Step((time-1.75*OB))
                 -(1.25)*Step((time-2*OB))+(0.75)*Step((time-2.25*OB))-(0.75)*Step((time-2.5*OB))-Step((time-3*OB))
                 +(0.5)*Step((time-3.25*OB))-(0.5)*Step((time-3.5));
    }
    else if(serialPass == 68)                                   //Complex
    {
        goBack = -(0.5)*Step((time-0.5*OB))+(0.5)*Step((time-0.75*OB))-(0.75)*Step((time-1.25*OB))-(1.25)*Step((time-2*OB))
                +(0.5)*Step((time-2.25*OB))+Step((time-2.5*OB))-(2.25)*Step((time-2.75*OB))+(0.75)*Step((time-3*OB))
                -(1.5)*Step((time-3.5*OB));
    }

    /*else if(serialPass == 56)                                      //Flanger
    {
        double wave = 0.5*sin(3*time);

       goBack = -0.5*Step(time) + wave;
    }
    */
    
    /*else if(serialPass == 57)                                      //1/4 Pitch Down
    {
       goBack = -(0.25)*Step(time-(0.25)*oneBeat)+Ramp(time, (time-(0.25)*oneBeat), 0.04)-(0.26)*Step(time-(0.5)*oneBeat)+Ramp(time, (time-(0.5)*oneBeat), 0.08)
                -(0.28)*Step(time-(0.75)*oneBeat)+Ramp(time, (time-(0.75)*oneBeat), 0.12)-(0.31)*Step(time-(1)*oneBeat)+Ramp(time, (time-(1)*oneBeat), 0.16)
                -(0.35)*Step(time-(1.25)*oneBeat)+Ramp(time, (time-(1.25)*oneBeat), 0.2)-(0.40)*Step(time-(1.5)*oneBeat)+Ramp(time, (time-(1.5)*oneBeat), 0.24)
                -(0.46)*Step(time-(1.75)*oneBeat)+Ramp(time, (time-(1.75)*oneBeat), 0.28)-(0.53)*Step(time-(2)*oneBeat)+Ramp(time, (time-(2)*oneBeat), 0.32)
                -(0.61)*Step(time-(2.25)*oneBeat)+Ramp(time, (time-(2.25)*oneBeat), 0.36)-(0.7)*Step(time-(2.5)*oneBeat)+Ramp(time, (time-(2.5)*oneBeat), 0.4)
                -(0.80)*Step(time-(2.75)*oneBeat)+Ramp(time, (time-(2.75)*oneBeat), 0.44)-(0.91)*Step(time-(3)*oneBeat)+Ramp(time, (time-(3)*oneBeat), 0.48)
                -(1.03)*Step(time-(3.25)*oneBeat)+Ramp(time, (time-(3.25)*oneBeat), 0.52)-(1.16)*Step(time-(3.5)*oneBeat)+Ramp(time, (time-(3.5)*oneBeat), 0.56)
                -(1.3)*Step(time-(3.75)*oneBeat)+Ramp(time, (time-(3.75)*oneBeat), 0.6)-(1.45)*Step(time-(4)*oneBeat)+Ramp(time, (time-(4)*oneBeat), 0.64);
    }
    */
} //SET Time Machine end

//Time Machine
//links the playback pointer with selected time signal and sends altered audio data to the Audio Codec output channels
void timeMachine()
{
    if(goBack == 0)
    {
        dryPlayback();
    }
    else if(goBack < 0)
    {
    //output buffer audio
        fluxCapacitor = recIndex + goBack;

        if(fluxCapacitor < 0)
        {
            fluxCapacitor = fluxCapacitor + bufferEnd;
        }

        CodecDataOut.Channel[LEFT] = buffer[LEFT][fluxCapacitor];
        CodecDataOut.Channel[RIGHT] = buffer[RIGHT][fluxCapacitor];
     }

}//end Time Machine


//RECORD CURRENT SAMPLE
//************************
void recordCurrentSample()
{
    buffer[LEFT][recIndex] = CodecDataIn.Channel[LEFT];
    buffer[RIGHT][recIndex] = CodecDataIn.Channel[RIGHT];


    if (++recIndex >= bufferEnd) // implement circular buffer
        recIndex = 0;
}//end record current sample


//INCREMENT TAP TEMPO COUNTER CURRENT SAMPLE
//************************
void incTapTempoCounter()
{
    if(sampleCounter != 144000)
    {
        sampleCounter++;
    }
}//end incTapTempoCounter


//DRY PLAYBACK
//************************
void dryPlayback()
{
    CodecDataOut.Channel[LEFT] = CodecDataIn.Channel[LEFT];
    CodecDataOut.Channel[RIGHT] = CodecDataIn.Channel[RIGHT];
}//end dry playbackIndex



interrupt void Codec_ISR()
///////////////////////////////////////////////////////////////////////
// Purpose:   Codec interface interrupt service routine
//
// Input:     None
//
// Returns:   Nothing
//
// Calls:     CheckForOverrun, ReadCodecData, WriteCodecData
//
// Notes:     None
///////////////////////////////////////////////////////////////////////
{
    /* add any local variables here */
    //Uint32 newest;  // only used for infinite echo

    if(CheckForOverrun())                   // overrun error occurred (i.e. halted DSP)
        return;                             // so serial port is reset to recover

    CodecDataIn.UINT = ReadCodecData();     // get input data samples


    recordCurrentSample();
    incTapTempoCounter();

    if(activeButton == 0)//No Buttons Pressed
    {
        goBack = 0;
        time=0;
        //fluxCapacitor = 0;
        dryPlayback();
    }

    if(activeButton == 1)//BeatRepeat Button Pressed
    {
        setTimeMachine(serialStore);
        timeMachine();
        Time();
    }



    WriteCodecData(CodecDataOut.UINT);      // send output data to  port

}//end ISR
