1) Design program to blink one LED and shift back and forth among 8 LEDs.  

https://youtube.com/shorts/7YG5PbYDssg?feature=share

2) Make 2 LEDs at the two ends of 8 LEDs on the board blink and move in different 
directions and back.

https://youtube.com/shorts/4kQak3TL5d0?feature=share

Source Code:
  
  #!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from sys import version_info

if version_info.major == 3:
        raw_input = input


# Set 8 Pins for 8 LEDs.
LedPins = [17, 27, 22, 5, 6, 13, 26, 12]

# Define a function to print message at the beginning
def print_message():
        print ("========================================")
        print ("|                8 LEDs                 |")
        print ("|    ------------------------------     |")
        print ("|         LED0 connect to GPIO17        |")
        print ("|         LED1 connect to GPIO27        |")
        print ("|         LED2 connect to GPIO22        |")
        print ("|         LED3 connect to GPIO05        |")
        print ("|         LED4 connect to GPIO06        |")
        print ("|         LED5 connect to GPIO13        |")
        print ("|         LED6 connect to GPIO26        |")
        print ("|         LED7 connect to GPIO12        |")
        print ("|                                       |")
        print ("|            Flow LED effect            |")
        print ("|                                       |")
        print ("|                             SunFounder|")
        print ("========================================\n")
        print ("Program is running...")
        print ("Please press Ctrl+C to end the program...")
        raw_input ("Press Enter to begin\n")

# Define a setup function for some setup
def setup():
        # Set the GPIO modes to BCM Numbering
        GPIO.setmode(GPIO.BCM)
        # Set all LedPin's mode to output, 
        # and initial level to High(3.3v)
        GPIO.setup(LedPins, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
        # Print messages
        print_message()
        leds = ['-', '-', '-', '-', '-', '-', '-', '-']
        while True:
                for pin in range(len(LedPins)):
                        #print pin
                        GPIO.output(LedPins[pin], GPIO.LOW)
                        GPIO.output(LedPins[len(LedPins)-1-pin], GPIO.LOW)
                        #leds[LedPins.index(pin)] = 0    # Show which led >
                        #print (leds)
                        time.sleep(0.1)
                        GPIO.output(LedPins[pin], GPIO.HIGH)
                        GPIO.output(LedPins[len(LedPins)-1-pin], GPIO.HIGH)
                        #leds[LedPins.index(pin)] = '-'  # Show the led is>



                # Turn LED off from right to left
                # print ("From right to left.")
                # for pin in reversed(LedPins):
                #         #print pin
                #         GPIO.output(pin, GPIO.LOW)
                #         leds[LedPins.index(pin)] = 0    # Show which led >
                #         print (leds)
                #         time.sleep(0.1)
                #         GPIO.output(pin, GPIO.HIGH)
                #         leds[LedPins.index(pin)] = '-'  # Show the led is>

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
        # Turn off all LEDs
        GPIO.output(LedPins, GPIO.HIGH)
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
 

3) Make 2 LEDs in the center blink in different directions and move back.

https://youtube.com/shorts/PIFcZi7PLX4?feature=share

Source Code:
  from gpiozero import LED
import time


led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(5)
led5 = LED(6)
led6 = LED(13)
led7 = LED(26)
led8 = LED(12)

while True:
    for led in [led1, led2, led3, led4]:
        led.on()
        time.sleep(0.5)
        led.off()
    
    for led in[led4, led3, led2, led1]:
        led.on()
        time.sleep(0.5)
        led.off()
      
    for led in [led8, led7, led6, led5]:
        led.on()
        time.sleep(0.5)
        led.off()
    
    for led in [led5, led6, led7, led8]:
        led.on()
        time.sleep(0.5)
        led.off()
    

  
  
  

