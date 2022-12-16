1) Build up the hardware circuit and run the example program to observe what will happen.

https://youtube.com/shorts/KTaPvt8RvrE?feature=share

2) Design the program to periodically display "A" and "B" in one LED dot matrix.

NOTE: I tried making it work with the below code, but it's not displaying the alphabets, professor...I did my best but it's not working. 
I apologize. I will work hard on it.

Source Code:
  
import RPi.GPIO as GPIO
import time
SDI = 17 
RCLK = 18 
SRCLK = 27

# Define the patterns for displaying the alphabets A and B
# Rows  ++++
code_H_A = [0x01, 0xff, 0x80, 0xff, 0x01]
# Columns ----
code_L_A = [0x00, 0x7f, 0x00, 0xfe, 0x00]

# Rows  ++++
code_H_B = [0x01, 0xff, 0x80, 0xff, 0x01, 0x02, 0x04, 0x08]
# Columns ----
code_L_B = [0x00, 0x7f, 0x00, 0xfe, 0x00, 0x00, 0x00, 0x00]


def setup():
    GPIO.setmode(GPIO.BCM) # Number GPIOs by its BCM location GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW) 
    GPIO.output(RCLK, GPIO.LOW) 
    GPIO.output(SRCLK, GPIO.LOW)
# Shift the data to 74HC595
def hc595_shift(dat): 
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit)) 
        GPIO.output(SRCLK, GPIO.HIGH) 
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW) 
        GPIO.output(RCLK, GPIO.HIGH) 
        time.sleep(0.001) 
        GPIO.output(RCLK, GPIO.LOW)

def main(): 
    while True:
        for i in range(0, len(code_H_A)):
            hc595_shift(code_L_A[i])
            hc595_shift(code_H_A[i])
            time.sleep(0.1)

        for i in range(0, len(code_H_B)):
            hc595_shift(code_L_B[i])
            hc595_shift(code_H_B[i])
            time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
