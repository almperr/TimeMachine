
//Author: Alexander Perr
//Project: Delay-Based Audio Effect Module
//Purpose: wait for button presses and send characters via UART to the Raspberry Pi which inturn control the DSP 


const int button1Pin = 4;     // the number of the pushbutton pin
const int button2Pin = 7;
const int button3Pin = 12;
const int button4Pin = 11;
const int button5Pin = 3; 
const int button6Pin = 6;
const int button7Pin = 9;
const int button8Pin = 10;
const int button9Pin = 2;
const int button10Pin = 5; 
const int button11Pin = 8;
const int button12Pin = 13;

// variables will change
int button1State = 0;         // variable for reading the pushbutton status
int button2State = 0;
int button3State = 0;
int button4State = 0;
int button5State = 0;
int button6State = 0;
int button7State = 0;
int button8State = 0;
int button9State = 0;
int button10State = 0;
int button11State = 0;
int button12State = 0;

void setup() 
{
  Serial.begin(115200);
  // initialize the pushbutton pin as an input:
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button3Pin, INPUT);
  pinMode(button4Pin, INPUT);
  pinMode(button5Pin, INPUT);
  pinMode(button6Pin, INPUT);
  pinMode(button7Pin, INPUT);
  pinMode(button8Pin, INPUT);
  pinMode(button9Pin, INPUT);
  pinMode(button10Pin, INPUT);
  pinMode(button11Pin, INPUT);
  pinMode(button12Pin, INPUT);
  
}

void loop() 
{
  // read the state of the pushbutton value:
  button1State = digitalRead(button1Pin);
  button2State = digitalRead(button2Pin);
  button3State = digitalRead(button3Pin);
  button4State = digitalRead(button4Pin);
  button5State = digitalRead(button5Pin);
  button6State = digitalRead(button6Pin);
  button7State = digitalRead(button7Pin);
  button8State = digitalRead(button8Pin);
  button9State = digitalRead(button9Pin);
  button10State = digitalRead(button10Pin);
  button11State = digitalRead(button11Pin);
  button12State = digitalRead(button12Pin);
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH and will send unique ASCII characters to Raspberry Pi
  if (button1State == HIGH) 
  {
    Serial.print(1);
    delay(30);
    while (button1State == HIGH) 
    {
      button1State = digitalRead(button1Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button2State == HIGH) 
  {
    Serial.print(2);
    delay(30);
    while (button2State == HIGH) 
    {
      button2State = digitalRead(button2Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button3State == HIGH) 
  {
    Serial.print(3);
    delay(30);
    while (button3State == HIGH) 
    {
      button3State = digitalRead(button3Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button4State == HIGH) 
  {
    Serial.print(4);
    delay(30);
    while (button4State == HIGH) 
    {
      button4State = digitalRead(button4Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button5State == HIGH) 
  {
    Serial.print(5);
    delay(30);
    while (button5State == HIGH) 
    {
      button5State = digitalRead(button5Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button6State == HIGH) 
  {
    Serial.print(6);
    delay(30);
    while (button6State == HIGH) 
    {
      button6State = digitalRead(button6Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button7State == HIGH) 
  {
    Serial.print(7);
    delay(30);
    while (button7State == HIGH) 
    {
      button7State = digitalRead(button7Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button8State == HIGH) 
  {
    Serial.print(8);
    delay(30);
    while (button8State == HIGH) 
    {
      button8State = digitalRead(button8Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button9State == HIGH) 
  {
    Serial.print(9);
    delay(30);
    while (button9State == HIGH) 
    {
      button9State = digitalRead(button9Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button10State == HIGH) 
  {
    Serial.print("!");
    delay(30);
    while (button10State == HIGH) 
    {
      button10State = digitalRead(button10Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button11State == HIGH) 
  {
    Serial.print("@");
    delay(30);
    while (button11State == HIGH) 
    {
      button11State = digitalRead(button11Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

  if (button12State == HIGH) 
  {
    Serial.print("#");
    delay(30);
    while (button12State == HIGH) 
    {
      button12State = digitalRead(button12Pin);
      ;
    }
    delay(30);
    Serial.print(0);
    
  }

}
