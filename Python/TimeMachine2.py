#Author: Alex Perr
#Project: Time Machine 
#Purpose: This code creates the GUI and sends and reveives commands to and from the other devices, TI OMAP-L138 and Arduino. 

import Tkinter as tk
import serial
import time

#initialize Serial Devices
arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, writeTimeout=0)
omap = serial.Serial('/dev/ttyUSB1', 115200, timeout=5)

#Global Variables
LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)

#Used to correspond effects selection to different buttons
BUTTON_SELECTED = 0  
TEXT_1 = "Mod 1"
TEXT_2 = "Mod 2"
TEXT_3 = "Mod 3"
TEXT_4 = "Mod 4"
TEXT_5 = "Mod 5"
TEXT_6 = "Mod 6"
TEXT_7 = "Mod 7"
TEXT_8 = "Mod 8"
TEXT_9 = "Mod 9"
TEXT_10 = "Mod 10"
TEXT_11 = "Mod 11"
TEXT_12 = "Mod 12"

#global variables used to program the different buttons, initially an empty string

serBuffer = ""
programButton1 = ''
programButton2 = ''
programButton3 = ''
programButton4 = ''
programButton5 = ''
programButton6 = ''
programButton7 = ''
programButton8 = ''
programButton9 = ''
programButton10 = ''
programButton11 = ''
programButton12 = ''

#FUNCTIONS

##serial function
def readSerial():
    while True:

        #include global variables for the buttons
        global programButton1
        
        c = arduino.read() # attempt to read a character from Serial
        
        #was anything read?
        if len(c) == 0:
            break
        
        print c
        
        #button pressed from Arduino 
        if c == '0':
            omap.write(b'0')
            omap.write(b'0')
            omap.write(b'0')    
        if c == '1':
            omap.write(str(programButton1).encode('ascii'))
            omap.write(str(programButton1).encode('ascii'))
            omap.write(str(programButton1).encode('ascii'))
        if c == '2':
            omap.write(str(programButton2).encode('ascii'))
            omap.write(str(programButton2).encode('ascii'))
            omap.write(str(programButton2).encode('ascii'))
        if c == '3':
            omap.write(str(programButton3).encode('ascii'))
            omap.write(str(programButton3).encode('ascii'))
            omap.write(str(programButton3).encode('ascii'))
        if c == '4':
            omap.write(str(programButton4).encode('ascii'))
            omap.write(str(programButton4).encode('ascii'))
            omap.write(str(programButton4).encode('ascii'))
        if c == '5':
            omap.write(str(programButton5).encode('ascii'))
            omap.write(str(programButton5).encode('ascii'))
            omap.write(str(programButton5).encode('ascii'))
        if c == '6':
            omap.write(str(programButton6).encode('ascii'))
            omap.write(str(programButton6).encode('ascii'))
            omap.write(str(programButton6).encode('ascii'))
        if c == '7':
            omap.write(str(programButton7).encode('ascii'))
            omap.write(str(programButton7).encode('ascii'))
            omap.write(str(programButton7).encode('ascii'))
        if c == '8':
            omap.write(str(programButton8).encode('ascii'))
            omap.write(str(programButton8).encode('ascii'))
            omap.write(str(programButton8).encode('ascii'))
        if c == '9':
            omap.write(str(programButton9).encode('ascii'))
            omap.write(str(programButton9).encode('ascii'))
            omap.write(str(programButton9).encode('ascii'))
        if c == '!':
            omap.write(str(programButton10).encode('ascii'))
            omap.write(str(programButton10).encode('ascii'))
            omap.write(str(programButton10).encode('ascii'))
        if c == '@':
            omap.write(str(programButton11).encode('ascii'))
            omap.write(str(programButton11).encode('ascii'))
            omap.write(str(programButton11).encode('ascii'))
        if c == '#':
            omap.write(str(programButton12).encode('ascii'))
            omap.write(str(programButton12).encode('ascii'))
            omap.write(str(programButton12).encode('ascii'))
        
    app.after(10, readSerial) # check serial again soon

##command to Tap Tempo
def tapTempo(self):
    print("tapTempo Pressed")
    omap.write(b'!')

##command to Shift Tempo Up
def shiftUp(self):
    omap.write(b'"')

##command to Shift Tempo Down
def shiftDown(self):
    omap.write(b'#')

##command to cut the Shift Off after the object is pressed in order to cease sending command
def shiftOff(self):
    omap.write(b'0')
    omap.write(b'0')
    omap.write(b'0')
    
##selects 
def select1(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 1
def select2(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 2
def select3(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 3
def select4(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 4
def select5(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 5
def select6(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 6
def select7(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 7
def select8(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 8
def select9(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 9
def select10(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 10
def select11(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 11
def select12(self):
    global BUTTON_SELECTED
    BUTTON_SELECTED = 12
    
##Effect1 Press
def Effect1Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '1'
    if BUTTON_SELECTED == 2:
        programButton2 = '1'
    if BUTTON_SELECTED == 3:
        programButton3 = '1'
    if BUTTON_SELECTED == 4:
        programButton4 = '1'
    if BUTTON_SELECTED == 5:
        programButton5 = '1'
    if BUTTON_SELECTED == 6:
        programButton6 = '1'
    if BUTTON_SELECTED == 7:
        programButton7 = '1'
    if BUTTON_SELECTED == 8:
        programButton8 = '1'
    if BUTTON_SELECTED == 9:
        programButton9 = '1'
    if BUTTON_SELECTED == 10:
        programButton10 = '1'
    if BUTTON_SELECTED == 11:
        programButton11 = '1'
    if BUTTON_SELECTED == 12:
        programButton12 = '1'
    else:
        pass
    
##Effect2 Press
def Effect2Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '2'
    if BUTTON_SELECTED == 2:
        programButton2 = '2'
    if BUTTON_SELECTED == 3:
        programButton3 = '2'
    if BUTTON_SELECTED == 4:
        programButton4 = '2'
    if BUTTON_SELECTED == 5:
        programButton5 = '2'
    if BUTTON_SELECTED == 6:
        programButton6 = '2'
    if BUTTON_SELECTED == 7:
        programButton7 = '2'
    if BUTTON_SELECTED == 8:
        programButton8 = '2'
    if BUTTON_SELECTED == 9:
        programButton9 = '2'
    if BUTTON_SELECTED == 10:
        programButton10 = '2'
    if BUTTON_SELECTED == 11:
        programButton11 = '2'
    if BUTTON_SELECTED == 12:
        programButton12 = '2'
    else:
        pass

##Effect3 Press
def Effect3Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '3'
    if BUTTON_SELECTED == 2:
        programButton2 = '3'
    if BUTTON_SELECTED == 3:
        programButton3 = '3'
    if BUTTON_SELECTED == 4:
        programButton4 = '3'
    if BUTTON_SELECTED == 5:
        programButton5 = '3'
    if BUTTON_SELECTED == 6:
        programButton6 = '3'
    if BUTTON_SELECTED == 7:
        programButton7 = '3'
    if BUTTON_SELECTED == 8:
        programButton8 = '3'
    if BUTTON_SELECTED == 9:
        programButton9 = '3'
    if BUTTON_SELECTED == 10:
        programButton10 = '3'
    if BUTTON_SELECTED == 11:
        programButton11 = '3'
    if BUTTON_SELECTED == 12:
        programButton12 = '3'
    else:
        pass

##Effect4 Press
def Effect4Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '4'
    if BUTTON_SELECTED == 2:
        programButton2 = '4'
    if BUTTON_SELECTED == 3:
        programButton3 = '4'
    if BUTTON_SELECTED == 4:
        programButton4 = '4'
    if BUTTON_SELECTED == 5:
        programButton5 = '4'
    if BUTTON_SELECTED == 6:
        programButton6 = '4'
    if BUTTON_SELECTED == 7:
        programButton7 = '4'
    if BUTTON_SELECTED == 8:
        programButton8 = '4'
    if BUTTON_SELECTED == 9:
        programButton9 = '4'
    if BUTTON_SELECTED == 10:
        programButton10 = '4'
    if BUTTON_SELECTED == 11:
        programButton11 = '4'
    if BUTTON_SELECTED == 12:
        programButton12 = '4'
    else:
        pass

    ##Effect5 Press
def Effect5Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '5'
    if BUTTON_SELECTED == 2:
        programButton2 = '5'
    if BUTTON_SELECTED == 3:
        programButton3 = '5'
    if BUTTON_SELECTED == 4:
        programButton4 = '5'
    if BUTTON_SELECTED == 5:
        programButton5 = '5'
    if BUTTON_SELECTED == 6:
        programButton6 = '5'
    if BUTTON_SELECTED == 7:
        programButton7 = '5'
    if BUTTON_SELECTED == 8:
        programButton8 = '5'
    if BUTTON_SELECTED == 9:
        programButton9 = '5'
    if BUTTON_SELECTED == 10:
        programButton10 = '5'
    if BUTTON_SELECTED == 11:
        programButton11 = '5'
    if BUTTON_SELECTED == 12:
        programButton12 = '5'
    else:
        pass

##Effect6 Press
def Effect6Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '6'
    if BUTTON_SELECTED == 2:
        programButton2 = '6'
    if BUTTON_SELECTED == 3:
        programButton3 = '6'
    if BUTTON_SELECTED == 4:
        programButton4 = '6'
    if BUTTON_SELECTED == 5:
        programButton5 = '6'
    if BUTTON_SELECTED == 6:
        programButton6 = '6'
    if BUTTON_SELECTED == 7:
        programButton7 = '6'
    if BUTTON_SELECTED == 8:
        programButton8 = '6'
    if BUTTON_SELECTED == 9:
        programButton9 = '6'
    if BUTTON_SELECTED == 10:
        programButton10 = '6'
    if BUTTON_SELECTED == 11:
        programButton11 = '6'
    if BUTTON_SELECTED == 12:
        programButton12 = '6'
    else:
        pass

##Effect7 Press
def Effect7Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '7'
    if BUTTON_SELECTED == 2:
        programButton2 = '7'
    if BUTTON_SELECTED == 3:
        programButton3 = '7'
    if BUTTON_SELECTED == 4:
        programButton4 = '7'
    if BUTTON_SELECTED == 5:
        programButton5 = '7'
    if BUTTON_SELECTED == 6:
        programButton6 = '7'
    if BUTTON_SELECTED == 7:
        programButton7 = '7'
    if BUTTON_SELECTED == 8:
        programButton8 = '7'
    if BUTTON_SELECTED == 9:
        programButton9 = '7'
    if BUTTON_SELECTED == 10:
        programButton10 = '7'
    if BUTTON_SELECTED == 11:
        programButton11 = '7'
    if BUTTON_SELECTED == 12:
        programButton12 = '7'
    else:
        pass

##Effect8 Press
def Effect8Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '8'
    if BUTTON_SELECTED == 2:
        programButton2 = '8'
    if BUTTON_SELECTED == 3:
        programButton3 = '8'
    if BUTTON_SELECTED == 4:
        programButton4 = '8'
    if BUTTON_SELECTED == 5:
        programButton5 = '8'
    if BUTTON_SELECTED == 6:
        programButton6 = '8'
    if BUTTON_SELECTED == 7:
        programButton7 = '8'
    if BUTTON_SELECTED == 8:
        programButton8 = '8'
    if BUTTON_SELECTED == 9:
        programButton9 = '8'
    if BUTTON_SELECTED == 10:
        programButton10 = '8'
    if BUTTON_SELECTED == 11:
        programButton11 = '8'
    if BUTTON_SELECTED == 12:
        programButton12 = '8'
    else:
        pass
    
    ##Effect9 Press
def Effect9Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '9'
    if BUTTON_SELECTED == 2:
        programButton2 = '9'
    if BUTTON_SELECTED == 3:
        programButton3 = '9'
    if BUTTON_SELECTED == 4:
        programButton4 = '9'
    if BUTTON_SELECTED == 5:
        programButton5 = '9'
    if BUTTON_SELECTED == 6:
        programButton6 = '9'
    if BUTTON_SELECTED == 7:
        programButton7 = '9'
    if BUTTON_SELECTED == 8:
        programButton8 = '9'
    if BUTTON_SELECTED == 9:
        programButton9 = '9'
    if BUTTON_SELECTED == 10:
        programButton10 = '9'
    if BUTTON_SELECTED == 11:
        programButton11 = '9'
    if BUTTON_SELECTED == 12:
        programButton12 = '9'
    else:
        pass

    ##Effect10 Press
def Effect10Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = ':'
    if BUTTON_SELECTED == 2:
        programButton2 = ':'
    if BUTTON_SELECTED == 3:
        programButton3 = ':'
    if BUTTON_SELECTED == 4:
        programButton4 = ':'
    if BUTTON_SELECTED == 5:
        programButton5 = ':'
    if BUTTON_SELECTED == 6:
        programButton6 = ':'
    if BUTTON_SELECTED == 7:
        programButton7 = ':'
    if BUTTON_SELECTED == 8:
        programButton8 = ':'
    if BUTTON_SELECTED == 9:
        programButton9 = ':'
    if BUTTON_SELECTED == 10:
        programButton10 = ':'
    if BUTTON_SELECTED == 11:
        programButton11 = ':'
    if BUTTON_SELECTED == 12:
        programButton12 = ':'
    else:
        pass
    
##Effect11 Press
def Effect11Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = ';'
    if BUTTON_SELECTED == 2:
        programButton2 = ';'
    if BUTTON_SELECTED == 3:
        programButton3 = ';'
    if BUTTON_SELECTED == 4:
        programButton4 = ';'
    if BUTTON_SELECTED == 5:
        programButton5 = ';'
    if BUTTON_SELECTED == 6:
        programButton6 = ';'
    if BUTTON_SELECTED == 7:
        programButton7 = ';'
    if BUTTON_SELECTED == 8:
        programButton8 = ';'
    if BUTTON_SELECTED == 9:
        programButton9 = ';'
    if BUTTON_SELECTED == 10:
        programButton10 = ';'
    if BUTTON_SELECTED == 11:
        programButton11 = ';'
    if BUTTON_SELECTED == 12:
        programButton12 = ';'
    else:
        pass

##Effect12 Press
def Effect12Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '<'
    if BUTTON_SELECTED == 2:
        programButton2 = '<'
    if BUTTON_SELECTED == 3:
        programButton3 = '<'
    if BUTTON_SELECTED == 4:
        programButton4 = '<'
    if BUTTON_SELECTED == 5:
        programButton5 = '<'
    if BUTTON_SELECTED == 6:
        programButton6 = '<'
    if BUTTON_SELECTED == 7:
        programButton7 = '<'
    if BUTTON_SELECTED == 8:
        programButton8 = '<'
    if BUTTON_SELECTED == 9:
        programButton9 = '<'
    if BUTTON_SELECTED == 10:
        programButton10 = '<'
    if BUTTON_SELECTED == 11:
        programButton11 = '<'
    if BUTTON_SELECTED == 12:
        programButton12 = '<'
    else:
        pass

##Effect13 Press
def Effect13Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '='
    if BUTTON_SELECTED == 2:
        programButton2 = '='
    if BUTTON_SELECTED == 3:
        programButton3 = '='
    if BUTTON_SELECTED == 4:
        programButton4 = '='
    if BUTTON_SELECTED == 5:
        programButton5 = '='
    if BUTTON_SELECTED == 6:
        programButton6 = '='
    if BUTTON_SELECTED == 7:
        programButton7 = '='
    if BUTTON_SELECTED == 8:
        programButton8 = '='
    if BUTTON_SELECTED == 9:
        programButton9 = '='
    if BUTTON_SELECTED == 10:
        programButton10 = '='
    if BUTTON_SELECTED == 11:
        programButton11 = '='
    if BUTTON_SELECTED == 12:
        programButton12 = '='
    else:
        pass

##Effect14 Press
def Effect14Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '>'
    if BUTTON_SELECTED == 2:
        programButton2 = '>'
    if BUTTON_SELECTED == 3:
        programButton3 = '>'
    if BUTTON_SELECTED == 4:
        programButton4 = '>'
    if BUTTON_SELECTED == 5:
        programButton5 = '>'
    if BUTTON_SELECTED == 6:
        programButton6 = '>'
    if BUTTON_SELECTED == 7:
        programButton7 = '>'
    if BUTTON_SELECTED == 8:
        programButton8 = '>'
    if BUTTON_SELECTED == 9:
        programButton9 = '>'
    if BUTTON_SELECTED == 10:
        programButton10 = '>'
    if BUTTON_SELECTED == 11:
        programButton11 = '>'
    if BUTTON_SELECTED == 12:
        programButton12 = '>'
    else:
        pass

##Effect15 Press
def Effect15Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '?'
    if BUTTON_SELECTED == 2:
        programButton2 = '?'
    if BUTTON_SELECTED == 3:
        programButton3 = '?'
    if BUTTON_SELECTED == 4:
        programButton4 = '?'
    if BUTTON_SELECTED == 5:
        programButton5 = '?'
    if BUTTON_SELECTED == 6:
        programButton6 = '?'
    if BUTTON_SELECTED == 7:
        programButton7 = '?'
    if BUTTON_SELECTED == 8:
        programButton8 = '?'
    if BUTTON_SELECTED == 9:
        programButton9 = '?'
    if BUTTON_SELECTED == 10:
        programButton10 = '?'
    if BUTTON_SELECTED == 11:
        programButton11 = '?'
    if BUTTON_SELECTED == 12:
        programButton12 = '?'
    else:
        pass

##Effect16 Press
def Effect16Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = '@'
    if BUTTON_SELECTED == 2:
        programButton2 = '@'
    if BUTTON_SELECTED == 3:
        programButton3 = '@'
    if BUTTON_SELECTED == 4:
        programButton4 = '@'
    if BUTTON_SELECTED == 5:
        programButton5 = '@'
    if BUTTON_SELECTED == 6:
        programButton6 = '@'
    if BUTTON_SELECTED == 7:
        programButton7 = '@'
    if BUTTON_SELECTED == 8:
        programButton8 = '@'
    if BUTTON_SELECTED == 9:
        programButton9 = '@'
    if BUTTON_SELECTED == 10:
        programButton10 = '@'
    if BUTTON_SELECTED == 11:
        programButton11 = '@'
    if BUTTON_SELECTED == 12:
        programButton12 = '@'
    else:
        pass

##Effect17 Press
def Effect17Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'A'
    if BUTTON_SELECTED == 2:
        programButton2 = 'A'
    if BUTTON_SELECTED == 3:
        programButton3 = 'A'
    if BUTTON_SELECTED == 4:
        programButton4 = 'A'
    if BUTTON_SELECTED == 5:
        programButton5 = 'A'
    if BUTTON_SELECTED == 6:
        programButton6 = 'A'
    if BUTTON_SELECTED == 7:
        programButton7 = 'A'
    if BUTTON_SELECTED == 8:
        programButton8 = 'A'
    if BUTTON_SELECTED == 9:
        programButton9 = 'A'
    if BUTTON_SELECTED == 10:
        programButton10 = 'A'
    if BUTTON_SELECTED == 11:
        programButton11 = 'A'
    if BUTTON_SELECTED == 12:
        programButton12 = 'A'
    else:
        pass

##Effect18 Press
def Effect18Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'B'
    if BUTTON_SELECTED == 2:
        programButton2 = 'B'
    if BUTTON_SELECTED == 3:
        programButton3 = 'B'
    if BUTTON_SELECTED == 4:
        programButton4 = 'B'
    if BUTTON_SELECTED == 5:
        programButton5 = 'B'
    if BUTTON_SELECTED == 6:
        programButton6 = 'B'
    if BUTTON_SELECTED == 7:
        programButton7 = 'B'
    if BUTTON_SELECTED == 8:
        programButton8 = 'B'
    if BUTTON_SELECTED == 9:
        programButton9 = 'B'
    if BUTTON_SELECTED == 10:
        programButton10 = 'B'
    if BUTTON_SELECTED == 11:
        programButton11 = 'B'
    if BUTTON_SELECTED == 12:
        programButton12 = 'B'
    else:
        pass

##Effect19 Press
def Effect19Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'C'
    if BUTTON_SELECTED == 2:
        programButton2 = 'C'
    if BUTTON_SELECTED == 3:
        programButton3 = 'C'
    if BUTTON_SELECTED == 4:
        programButton4 = 'C'
    if BUTTON_SELECTED == 5:
        programButton5 = 'C'
    if BUTTON_SELECTED == 6:
        programButton6 = 'C'
    if BUTTON_SELECTED == 7:
        programButton7 = 'C'
    if BUTTON_SELECTED == 8:
        programButton8 = 'C'
    if BUTTON_SELECTED == 9:
        programButton9 = 'C'
    if BUTTON_SELECTED == 10:
        programButton10 = 'C'
    if BUTTON_SELECTED == 11:
        programButton11 = 'C'
    if BUTTON_SELECTED == 12:
        programButton12 = 'C'
    else:
        pass

##Effect20 Press
def Effect20Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'D'
    if BUTTON_SELECTED == 2:
        programButton2 = 'D'
    if BUTTON_SELECTED == 3:
        programButton3 = 'D'
    if BUTTON_SELECTED == 4:
        programButton4 = 'D'
    if BUTTON_SELECTED == 5:
        programButton5 = 'D'
    if BUTTON_SELECTED == 6:
        programButton6 = 'D'
    if BUTTON_SELECTED == 7:
        programButton7 = 'D'
    if BUTTON_SELECTED == 8:
        programButton8 = 'D'
    if BUTTON_SELECTED == 9:
        programButton9 = 'D'
    if BUTTON_SELECTED == 10:
        programButton10 = 'D'
    if BUTTON_SELECTED == 11:
        programButton11 = 'D'
    if BUTTON_SELECTED == 12:
        programButton12 = 'D'
    else:
        pass

##Effect21 Press
def Effect21Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'E'
    if BUTTON_SELECTED == 2:
        programButton2 = 'E'
    if BUTTON_SELECTED == 3:
        programButton3 = 'E'
    if BUTTON_SELECTED == 4:
        programButton4 = 'E'
    if BUTTON_SELECTED == 5:
        programButton5 = 'E'
    if BUTTON_SELECTED == 6:
        programButton6 = 'E'
    if BUTTON_SELECTED == 7:
        programButton7 = 'E'
    if BUTTON_SELECTED == 8:
        programButton8 = 'E'
    if BUTTON_SELECTED == 9:
        programButton9 = 'E'
    if BUTTON_SELECTED == 10:
        programButton10 = 'E'
    if BUTTON_SELECTED == 11:
        programButton11 = 'E'
    if BUTTON_SELECTED == 12:
        programButton12 = 'E'
    else:
        pass
    
    ##Effect22 Press
def Effect22Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'F'
    if BUTTON_SELECTED == 2:
        programButton2 = 'F'
    if BUTTON_SELECTED == 3:
        programButton3 = 'F'
    if BUTTON_SELECTED == 4:
        programButton4 = 'F'
    if BUTTON_SELECTED == 5:
        programButton5 = 'F'
    if BUTTON_SELECTED == 6:
        programButton6 = 'F'
    if BUTTON_SELECTED == 7:
        programButton7 = 'F'
    if BUTTON_SELECTED == 8:
        programButton8 = 'F'
    if BUTTON_SELECTED == 9:
        programButton9 = 'F'
    if BUTTON_SELECTED == 10:
        programButton10 = 'F'
    if BUTTON_SELECTED == 11:
        programButton11 = 'F'
    if BUTTON_SELECTED == 12:
        programButton12 = 'F'
    else:
        pass

    ##Effect23 Press
def Effect23Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'G'
    if BUTTON_SELECTED == 2:
        programButton2 = 'G'
    if BUTTON_SELECTED == 3:
        programButton3 = 'G'
    if BUTTON_SELECTED == 4:
        programButton4 = 'G'
    if BUTTON_SELECTED == 5:
        programButton5 = 'G'
    if BUTTON_SELECTED == 6:
        programButton6 = 'G'
    if BUTTON_SELECTED == 7:
        programButton7 = 'G'
    if BUTTON_SELECTED == 8:
        programButton8 = 'G'
    if BUTTON_SELECTED == 9:
        programButton9 = 'G'
    if BUTTON_SELECTED == 10:
        programButton10 = 'G'
    if BUTTON_SELECTED == 11:
        programButton11 = 'G'
    if BUTTON_SELECTED == 12:
        programButton12 = 'G'
    else:
        pass

##Effect24 Press
def Effect24Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'H'
    if BUTTON_SELECTED == 2:
        programButton2 = 'H'
    if BUTTON_SELECTED == 3:
        programButton3 = 'H'
    if BUTTON_SELECTED == 4:
        programButton4 = 'H'
    if BUTTON_SELECTED == 5:
        programButton5 = 'H'
    if BUTTON_SELECTED == 6:
        programButton6 = 'H'
    if BUTTON_SELECTED == 7:
        programButton7 = 'H'
    if BUTTON_SELECTED == 8:
        programButton8 = 'H'
    if BUTTON_SELECTED == 9:
        programButton9 = 'H'
    if BUTTON_SELECTED == 10:
        programButton10 = 'H'
    if BUTTON_SELECTED == 11:
        programButton11 = 'H'
    if BUTTON_SELECTED == 12:
        programButton12 = 'H'
    else:
        pass

##Effect25 Press
def Effect25Press(self):
    global BUTTON_SELECTED
    global programButton1
    global programButton2
    global programButton3
    global programButton4
    global programButton5
    global programButton6
    global programButton7
    global programButton8
    global programButton9
    global programButton10
    global programButton11
    global programButton12

    if BUTTON_SELECTED == 1:
        programButton1 = 'I'
    if BUTTON_SELECTED == 2:
        programButton2 = 'I'
    if BUTTON_SELECTED == 3:
        programButton3 = 'I'
    if BUTTON_SELECTED == 4:
        programButton4 = 'I'
    if BUTTON_SELECTED == 5:
        programButton5 = 'I'
    if BUTTON_SELECTED == 6:
        programButton6 = 'I'
    if BUTTON_SELECTED == 7:
        programButton7 = 'I'
    if BUTTON_SELECTED == 8:
        programButton8 = 'I'
    if BUTTON_SELECTED == 9:
        programButton9 = 'I'
    if BUTTON_SELECTED == 10:
        programButton10 = 'I'
    if BUTTON_SELECTED == 11:
        programButton11 = 'I'
    if BUTTON_SELECTED == 12:
        programButton12 = 'I'
    else:
        pass


#CLASSES

#this is the main class used to create the main page and the effects selection menu for each of the 12 customizable button modules
class MainClass(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        
        self.frames = {}

        for F in (MainMenu, ModOne, ModTwo, ModThree, ModFour, ModFive, ModSix, ModSeven, ModEight, ModNine, ModTen, ModEleven, ModTwelve):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(MainMenu)
                
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
#this is the main page, where the user selects the Arduino push button they wish to program
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, background='#184A4A')

        Mod1 = tk.Button(self, text = TEXT_1, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModOne))
        Mod1.bind('<Button>', select1)
        Mod1.grid(row=0, column=0)

        Mod2 = tk.Button(self, text = TEXT_2, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModTwo))
        Mod2.bind('<Button>', select2)
        Mod2.grid(row=0, column=1)
        
        Mod3 = tk.Button(self, text = TEXT_3, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModThree))
        Mod3.bind('<Button>', select3)
        Mod3.grid(row=0, column=2)

        Mod4 = tk.Button(self, text = TEXT_4, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModFour))
        Mod4.bind('<Button>', select4)
        Mod4.grid(row=0, column=3)

        Mod5 = tk.Button(self, text = TEXT_5, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModFive))
        Mod5.bind('<Button>', select5)
        Mod5.grid(row=1, column=0)

        Mod6 = tk.Button(self, text = TEXT_6, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModSix))
        Mod6.bind('<Button>', select6)
        Mod6.grid(row=1, column=1)

        Mod7 = tk.Button(self, text = TEXT_7, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModSeven))
        Mod7.bind('<Button>', select7)
        Mod7.grid(row=1, column=2)

        Mod8 = tk.Button(self, text = TEXT_8, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModEight))
        Mod8.bind('<Button>', select8)
        Mod8.grid(row=1, column=3)

        Mod9 = tk.Button(self, text = TEXT_9, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModNine))
        Mod9.bind('<Button>', select9)
        Mod9.grid(row=2, column=0)

        Mod10 = tk.Button(self, text = TEXT_10, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModTen))
        Mod10.bind('<Button>', select10)
        Mod10.grid(row=2, column=1)

        Mod11 = tk.Button(self, text = TEXT_11, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModEleven))
        Mod11.bind('<Button>', select11)
        Mod11.grid(row=2, column=2)

        Mod12 = tk.Button(self, text = TEXT_12, font = LARGE_FONT, height = 3, width = 6, background ='#62D5B4', activebackground='#83EEC5', command=lambda: controller.show_frame(ModTwelve))
        Mod12.bind('<Button>', select12)
        Mod12.grid(row=2, column=3)

        #tempoPress
        tempoPress = tk.Button(self, text = "Tap Tempo", font = LARGE_FONT, height = 5, width = 10, background ='#FF6A62', activebackground='#EE2039')
        tempoPress.place(x=352, y=0)
        tempoPress.bind('<Button>', tapTempo)

        tempoShiftUp = tk.Button(self, text = "Shift Tempo Up", font = SMALL_FONT, height = 2, width = 12, background = '#cdcdcd', activebackground = '#ffffff')
        tempoShiftUp.place(x=354, y=110)
        tempoShiftUp.bind('<Button>', shiftUp)
        tempoShiftUp.bind('<ButtonRelease>', shiftOff)
      
        tempoShiftDown = tk.Button(self, text = "Shift Tempo Down", font = SMALL_FONT, height = 2, width = 12, background = '#cdcdcd', activebackground = '#ffffff')
        tempoShiftDown.place(x=354, y=160)
        tempoShiftDown.bind('<Button>', shiftDown)
        tempoShiftDown.bind('<ButtonRelease>', shiftOff)

#Each module has their own effects selection menu page
class ModOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Mod 1", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)

        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)
        
class ModTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 2", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4) 

class ModThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 3", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)

        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 4", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)

        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)
        
class ModFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 5", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)

        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 6", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 7", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 8", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 9", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 10", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModEleven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 10", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

class ModTwelve(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Mod 12", font=LARGE_FONT)
        label.grid(row=0,column=0)

        back = tk.Button(self, text="back", command=lambda: controller.show_frame(MainMenu))
        back.grid(row=1,column=0)
        
        effect1 = tk.Button(self, text="1 Beat Rpt", background='#BDFF73', activebackground='#A4D541',font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect1.bind('<Button>', Effect1Press)
        effect1.grid(row=2, column=0)

        effect2 = tk.Button(self, text="1/2 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect2.bind('<Button>', Effect2Press)
        effect2.grid(row=3, column=0)

        effect3 = tk.Button(self, text="1/3 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect3.bind('<Button>', Effect3Press)
        effect3.grid(row=4, column=0)

        effect4 = tk.Button(self, text="1/4 Beat Rpt", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect4.bind('<Button>', Effect4Press)
        effect4.grid(row=5, column=0)

        effect5 = tk.Button(self, text="Reverse", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect5.bind('<Button>', Effect5Press)
        effect5.grid(row=6, column=0)

        effect6 = tk.Button(self, text="1/2 Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect6.bind('<Button>', Effect6Press)
        effect6.grid(row=2, column=1)

        effect7 = tk.Button(self, text="2X Speed", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect7.bind('<Button>', Effect7Press)
        effect7.grid(row=3, column=1)

        effect8 = tk.Button(self, text="Slow Triplet", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect8.bind('<Button>', Effect8Press)
        effect8.grid(row=4, column=1)

        effect9 = tk.Button(self, text="Backspin Start", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect9.bind('<Button>', Effect9Press)
        effect9.grid(row=5, column=1)

        effect10 = tk.Button(self, text="Vinyl Off", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect10.bind('<Button>', Effect10Press)
        effect10.grid(row=6, column=1)

        effect11 = tk.Button(self, text="Stutter 1", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect11.bind('<Button>', Effect11Press)
        effect11.grid(row=2, column=2)

        effect12 = tk.Button(self, text="Stutter 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect12.bind('<Button>', Effect12Press)
        effect12.grid(row=3, column=2)

        effect13 = tk.Button(self, text="Stutter 3", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect13.bind('<Button>', Effect13Press)
        effect13.grid(row=4, column=2)

        effect14 = tk.Button(self, text="Stutter 4", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect14.bind('<Button>', Effect14Press)
        effect14.grid(row=5, column=2)

        effect15 = tk.Button(self, text="Shuffle", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect15.bind('<Button>', Effect15Press)
        effect15.grid(row=6, column=2)

        effect16 = tk.Button(self, text="Shuffle 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect16.bind('<Button>', Effect16Press)
        effect16.grid(row=2, column=3)
 
        effect17 = tk.Button(self, text="Swing", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect17.bind('<Button>', Effect17Press)
        effect17.grid(row=3, column=3)

        effect18 = tk.Button(self, text="Basic", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect18.bind('<Button>', Effect18Press)
        effect18.grid(row=4, column=3)

        effect19 = tk.Button(self, text="Complex", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect19.bind('<Button>', Effect19Press)
        effect19.grid(row=5, column=3)

        effect20 = tk.Button(self, text="Complex 2", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect20.bind('<Button>', Effect20Press)
        effect20.grid(row=6, column=3)

        effect21 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect21.bind('<Button>', Effect21Press)
        effect21.grid(row=2, column=4)

        effect22 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect22.bind('<Button>', Effect22Press)
        effect22.grid(row=3, column=4)

        effect23 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect23.bind('<Button>', Effect23Press)
        effect23.grid(row=4, column=4)

        effect24 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect24.bind('<Button>', Effect24Press)
        effect24.grid(row=5, column=4)

        effect25 = tk.Button(self, text="Empty", background='#BDFF73', activebackground='#A4D541', font=SMALL_FONT, height = 2, width = 10, command=lambda: controller.show_frame(MainMenu))
        effect25.bind('<Button>', Effect25Press)
        effect25.grid(row=6, column=4)

app = MainClass()
app.configure(background='#184A4A', cursor = 'none')                    #sets background to be black and makes the cursor invisible
app.title("Time Machine V.2")                                           #set title of the program
app.geometry('480x280')
app.after(10, readSerial)
app.mainloop()
