#DC Motor Control

1) Build up the hardware circuit and run the example program to observe what will 
happen.

https://youtu.be/OhGMDoSCu_E
 
#I observed that the DC motor goes both clockwise and counterclockwise when the program is running.

2) Add two LEDs in the different colors of the yellow and red to the above circuit. 
And switch on the yellow one if the DC motor is running in the clockwise 
direction. Otherwise, switch on the red one.

https://youtube.com/shorts/r8zRlFQgLIg?feature=share
  
 Source Code:
  
 #!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from sys import version_info

if version_info.major == 3:
        raw_input = input

# Set up pins
MotorPin1   = 17
MotorPin2   = 18
MotorEnable = 27
LedPin = 4
LedPin2 = 5

def print_message():
        print ("========================================")
        print ("|                Motor                 |")
        print ("|    ------------------------------    |")
        print ("|     Motor pin 1 connect to GPIO17    |")
        print ("|     Motor pin 2 connect to GPIO18    |")
        print ("|     Motor enable connect to GPIO27   |")
        print ("|                                      |")
        print ("|         Controlling a motor          |")
        print ("|                                      |")
        print ("|                            SunFounder|")
        print ("======================================\n")
        print ("Program is running...")
        print ("Please press Ctrl+C to end the program...")
        raw_input ("Press Enter to begin\n")


def setup():
        # Set the GPIO modes to BCM Numbering
        GPIO.setmode(GPIO.BCM)
        # Set pins to output
        GPIO.setup(MotorPin1, GPIO.OUT)
        GPIO.setup(MotorPin2, GPIO.OUT)
        GPIO.setup(MotorEnable, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(LedPin2, GPIO.OUT, initial=GPIO.HIGH)

# Define a motor function to spin the motor
# direction should be 
# 1(clockwise), 0(stop), -1(counterclockwise)
def motor(direction):
        # Clockwise
        if direction == 1:
                # Set direction
                GPIO.output(MotorPin1, GPIO.HIGH)
                GPIO.output(MotorPin2, GPIO.LOW)
                # Enable the motor
                GPIO.output(MotorEnable, GPIO.HIGH)
                print ("Clockwise")
                GPIO.output(LedPin, GPIO.LOW)
                GPIO.output(LedPin2, GPIO.HIGH)
                time.sleep(0.5)
        # Counterclockwise
if direction == -1:
                # Set direction
                GPIO.output(MotorPin1, GPIO.LOW)
                GPIO.output(MotorPin2, GPIO.HIGH)
                # Enable the motor
                GPIO.output(MotorEnable, GPIO.HIGH)
                print ("Counterclockwise")
                GPIO.output(LedPin, GPIO.HIGH)
                GPIO.output(LedPin2, GPIO.LOW)
                time.sleep(0.5)
        # Stop
        if direction == 0:
                # Disable the motor
                GPIO.output(MotorEnable, GPIO.LOW)
                print ("Stop")
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LedPin2, GPIO.HIGH)
                time.sleep(0.5)

def main():
        print_message()
        # Define a dictionary to make the script more readable
        # CW as clockwise, CCW as counterclockwise, STOP as stop
        directions = {'CW': 1, 'CCW': -1, 'STOP': 0}
        while True:
                # Clockwise
                motor(directions['CW'])
                time.sleep(5)
                # Stop
                motor(directions['STOP'])
                # Anticlockwise
                motor(directions['CCW'])
                time.sleep(5)
                # Stop
                motor(directions['STOP'])
                time.sleep(5)
def destroy():
        # Stop the motor
        GPIO.output(MotorEnable, GPIO.LOW)
        GPIO.output(LedPin, GPIO.HIGH)
        GPIO.output(LedPin2, GPIO.HIGH)
        # Release resource
        GPIO.cleanup()    

# If run this script directly, do:
if __name__ == '__main__':
        setup()
        try:
                main()

        # When 'Ctrl+C' is pressed, the child program 
        # destroy() will be executed.
        except KeyboardInterrupt:
                destroy()



