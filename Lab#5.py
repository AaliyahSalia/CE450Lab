1) Implement the 7-segment LEDs control based on the above example program

https://youtube.com/shorts/0gavWrIjv-w

2) Add one more 7-segment LED to the above design for the continuous display of 
the decimal number from 1 to 25 and alphabet from A-Z display.

https://youtu.be/2WQyVi3Zfkc

Source Code:
  
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

SDI   = 17
RCLK  = 18
SRCLK = 27

SDI2 = 5
RCLK2 = 12
SRCLK2 = 25


segCode = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x5B, 0x5B, 0x5B, 0x5B, 0x5B, 0x5B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, >
segCode2 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x77, 0x7C, 0x58, 0x5E, 0x79, 0x71,>

def print_msg():
    print ("Program is running...")
    print ("Please press Ctrl+C to end the program...")

def setup():
    GPIO.setmode(GPIO.BCM)    #Number GPIOs by BCM
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)
    GPIO.setup(SDI2, GPIO.OUT)
    GPIO.setup(RCLK2, GPIO.OUT)
    GPIO.setup(SRCLK2, GPIO.OUT)
    GPIO.output(SDI2, GPIO.LOW)
    GPIO.output(RCLK2, GPIO.LOW)
    GPIO.output(SRCLK2, GPIO.LOW)
    
def hc595_shift(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def hc595_shift2(dat):
    for bit in range(0, 8):
        GPIO.output(SDI2, 0x80 & (dat << bit))
        GPIO.output(SRCLK2, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK2, GPIO.LOW)
    GPIO.output(RCLK2, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK2, GPIO.LOW)
    def loop():
    while True:
        for i in range(0, len(segCode)):
            hc595_shift(segCode[i])
            time.sleep(0.5)
            hc595_shift2(segCode2[i])
            time.sleep(1)

def destroy():   #When program ending, the function is executed.
    GPIO.cleanup()

if __name__ == '__main__': #Program starting from here
    print_msg()
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()




Thank you! 



             
