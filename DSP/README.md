## Welcome to the OMAP-L138 Code for Time Machine  

### Overview
This code is used to program the Texas Instruments OMAP-L138 Low-Cost Development Kit (LCDK) to perform necessary Digital Signal Processing operations for Time Machine. This code is produced in C using TI's Code Composer IDE. 

It starts by initializing all of the components, such as the audio codec and the DSP, and then allocates memory locations. It brings in audio signals from an external audio source connected by 3.5 mm audio jack. The analog audio signal is converted into a digital signal using the onboard Audio Codec (TI AIC3106 Audio Codec). The audio signal data is then stored in a rolling buffer, in SDRAM. This buffer size is determined by the BPM (Beats Per Minute) of the machine, set by the user, as slower songs need more memory than slower songs. The BPM is set in order to quantify how many samples are in 1 beat. The effects are carried out by using differential equations. The equations create different time signal envelopes that control a playback pointer. Time signals determine how far back in time the playback pointer goes, into the rolling buffer, over a 4 beat sequence. The playback pointer can go back up to 8 beats. The playback pointer selects what data to send to the audio codec. The audio codec converts digital data to an analog signal and then to the speaker; this includes dry audio. Activating different time signals creates different effects. The effects are activated based on the serial data that is received from the Raspberry Pi 3. This system is running at a sampling rate of 48 kHz. An Interrupt Service Routine is used to drive all DSP operations. 

### Hardware
The OMAP-L138 is a TI C6000 Series DSP + ARM Processor. The OMAP-L138 LCDK comes equipped with all of the necessary components needed for DSP operations of Time Machine, such as:
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
  - Differential equations to create time delay signals that change playback pointer over time, creates delay based effects
  - Interrupt Service Routine to drive DSP operations and maintain 48 kHz sampling rate

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



  
