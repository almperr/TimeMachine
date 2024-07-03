# Time Machine

### Introduction

Time Machine is a Delay-Based Audio Effects Module that can alter and remix audio in real time. Anybody can sound like a professional DJ with this machine. Time Machine is a powerful tool that can perform momentary rolling loops, rearrange rhythm, change playback speed, reverse, stutter, vinyl scratch effects, flanger effects, and other DJ effects over a 4 beat sequence. Effects are selected by a touch screen GUI. There are 12 push buttons that can each be programmed by the user to activate effects. There are 25 different audio effect sequences the user can choose from and program to the buttons. A Tap Tempo on the touch screen GUI is used in order to synchronize the device BPM (beats per minute) to the BPM of any song that is played through it. A music source and a speaker are plugged into 3.5mm audio input and output jacks. This is a working prototype programmed using Python and C. Inspiration for this machine came from a VST Plug-In called Gross Beat by Image Line. 

<img src="images/timemachine.JPG" width="500">

### Hardware

- **Texas Instruments OMAP-L138 LCDK** - Performs all of the Digital Signal Processing operations; receives commands from the Raspberry Pi 3

- **Raspberry Pi 3** - Used to create the touch screen GUI, receives commands from the Arduino Nano, and sends commands to the OMAP-L138 LCDK via USB 

- **Arduino Nano** - Used to create the 12 button push button pad and send messages to the Raspberry Pi 3 via USB

- **Uctronics 3.5 inch TFT touch screen** - is the touch screen for the device; connected to pins and HDMI to the Raspberry Pi 3

### Folders and Purpose

- **TimeMachine/Arduino** - Contains C code written in order to program the Arduino Nano

- **TimeMachine/DSP** - Contains the C code for real-time DSP operations on the TI OMAP-L138 Low Cost Development Kit (LCDK)

- **TimeMachine/Python** - Contains Python code used to program the Raspberry Pi 3
