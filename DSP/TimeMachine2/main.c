 
///////////////////////////////////////////////////////////////////////
// Filename: main.c
//
// Synopsis: Main program file for Time Machine DSP code
//
// Author: Alexander Perr
//
// Project: Time Machine 2 
//
///////////////////////////////////////////////////////////////////////

#include "DSP_Config.h"   
#include <stdio.h>

int main()
   {

    // initialize DSP board
    DSP_Init();
    Init_UART2(115200);

    // call StartUp for application specific code
    // defined in each application directory
    StartUp();

    // main stalls here, interrupts drive operation
    while(1)
    {
        Uint8 dataReady = IsDataReady_UART2();

        if(dataReady != 0)
        {
           Uint8 serialIn = Read_UART2();
           //change unsigned to int
           int serialNumber = (int)(serialIn);
           //printf("%d\n", serialNumber);        //comment out, used to test data coming in

           //select which function is called in ISR
           if (serialNumber == 33)
           {

             tapTempo();

           }
           else if(serialNumber == 34)
           {
               shiftTempoUp();
           }
           else if(serialNumber == 35)
           {
               shiftTempoDown();
           }
           else if (serialNumber != 48 && serialNumber <= 74)
           {

             //call set time machine function and pass the function selection data
             setTimeMachine(serialNumber);
           }
           else
           {

             //if no recognizable serial number is inputted, continue dry playback
             setActiveButton(0);

           }//else

        }//if

    }//while

}//main
