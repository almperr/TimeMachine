## Welcome to the OMAP-L138 Code for Time Machine  

### Overview
This code is used to program the Texas Instruments OMAP-L138 Low-Cost Development Kit (LCDK) to perform necessary Digital Signal Processing operations for the the prototype of the Delay-Based Audio Effects Module called Time Machine. This code is produced in C using TI's, IDE Code Composer. Time Machine utilizes delay-based audio effects that allow the user to be able to alter and remix music in real time. Time Machine has 25 different delay-based audio effects to choose from that allow the user to change the rhythm of any song in different ways. They also allow the user to perform momentary repeat loops, speed up, slow down, reverse, stutter, vinyl scratch effects, and change pitch. The user can load up to 12 different delay-based audio effects onto a push button pad so that the user can try different combinations of effects.     

The OMAP-L138 is a TI C6000 Series DSP + ARM Processor. The OMAP-L138 LCDK comes equipped with all of the necessary components needed for creating a working prototype of the device, such as:
  - 128 MByte DDR2 SDRAM running at 150MHz and 128 MByte 16-bit wide NAND FLASH
  - TI AIC3106 Audio Codec 
  - 3.5 mm audio jacks (audio input/output)
  - UART USB input
  
### Files and their contents

main.c
  - Initialize DSP, audio codec, and interrupt service routine
  - Check if Tap Tempo, Tempo Up, Tempo Down pressed
  - Check UART serial port to see if effect is activated
  - If effect activated, pass associated number to setTimeMachine()
  - If no button pressed, dry playback

ISRs_B.c
  - Define left and right audio channel buffer
  - Global variables 
  - Required functions to carry out delay-based audio effects
  - Send altered audio data to the audio codec output using Interrupt Service Routine 

LCDK_Support_DSP.c
  - Functions to support basic initialization of the OMAP-L138 hardware resources

LCDK_Support_DSP.h
  - Declarations for OMAPL138_Support_DSP.c

OMAPL138_defines.h
  - Register definitions
  
StartUp.c
  - Placeholder for code run after DSK_Init

tistdtypes.h
  - DSP/BIOS_Kernel


  
