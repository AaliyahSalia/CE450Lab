1) Build up the hardware circuit and run the example program to observe what will happen.

https://youtube.com/shorts/aVYYVtmBUzI?feature=share
  
I noticed that when I rotate the encoder clockwise, the value increases and when I rotate it counterclockwise, the value decreases.

2) Add a buzzer to the above circuit and design the program to make “z” sound as the turning indicator if the encoder is turned one circle 

https://youtube.com/shorts/EANfkzLzYYU?feature=share

Source Code:

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Set up pins
# Rotary A Pin
RoAPin = 17
# Rotary B Pin
RoBPin = 18
# Rotary Switch Pin
RoSPin = 27
BeepPin = 26
def print_message():
        print ("========================================")
        print ("|            Rotary Encoder            |")
        print ("|    ------------------------------    |")
        print ("|        Pin A connect to GPIO0        |")
        print ("|        Pin B connect to GPIO1        |")
        print ("|     Button Pin connect to GPIO 2     |")
        print ("|                                      |")
        print ("|         Use a Rotary Encoder         |")
        print ("|     Rotary to add/minus counter      |")
        print ("|      Press to set counter to 0       |")
        print ("|                                      |")
        print ("|                            SunFounder|")
        print ("========================================\n")
        print ('Program is running...')
        print ('Please press Ctrl+C to end the program...')
        print (input ("Press Enter to begin\n"))

def setup():
        global counter
        global Last_RoB_Status, Current_RoB_Status
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RoAPin, GPIO.IN)
        GPIO.setup(RoBPin, GPIO.IN)
        GPIO.setup(RoSPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # Set up a falling edge detect to callback clear
        GPIO.add_event_detect(RoSPin, GPIO.FALLING, callback=clear)
        GPIO.setup(BeepPin, GPIO.OUT, initial = GPIO.HIGH)

        # Set up a counter as a global variable
        counter = 0
        Last_RoB_Status = 0
        Current_RoB_Status = 0
# Define a function to deal with rotary encoder
def rotaryDeal():
        global counter
        global Last_RoB_Status, Current_RoB_Status

        flag = 0
        Last_RoB_Status = GPIO.input(RoBPin)
        # When RoAPin level changes
while(not GPIO.input(RoAPin)):
                Current_RoB_Status = GPIO.input(RoBPin)
                flag = 1
        if flag == 1:
                # Reset flag
                flag = 0
                if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
                        counter = counter + 1
                        GPIO.output(BeepPin, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(BeepPin, GPIO.HIGH)
                        time.sleep(0.5)

                if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
                        counter = counter - 1
                        GPIO.output(BeepPin, GPIO.HIGH)
                        time.sleep(0.1)
                print ('counter = %d' % counter)

# Define a callback function on switch, to clean "counter"
def clear(ev=None):
        global counter
        counter = 0

def main():
        print_message()
        while True:
                rotaryDeal()
        

def destroy():
        GPIO.output(BeepPin, GPIO.HIGH)
        # Release resource
        GPIO.cleanup()  

# If run this script directly, do:
if __name__ == '__main__':
        setup()
        try:
                main()
        # When 'Ctrl+C' is pressed, the child program 
        # destroy() will be  executed.
        except KeyboardInterrupt:
                destroy()


