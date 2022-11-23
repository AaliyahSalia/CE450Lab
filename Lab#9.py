1) Build up the hardware circuit and run the example program to observe what will happen.

After running the example, the LCD displays a message saying 'Greetings!!' (on the first line) and 'from SunFounder' (on the second line).

https://youtube.com/shorts/aUYaiUy4JBY?feature=share
 

Source Code:
  
#!/usr/bin/env python3
import smbus
import LCD1602
import time

bus = smbus.SMBus(1)
time.sleep(1) #wait here to avoid 121 IO Error

def setup():
        LCD1602.init(0x27, 1)   # init(slave address, background light)
        LCD1602.write(0, 0, 'Greetings!!')
        LCD1602.write(1, 1, 'from SunFounder')
        time.sleep(2)

def destroy():
        LCD1602.clear()

if __name__ == "__main__":
        try:
                setup()
        except KeyboardInterrupt:
                destroy()
            
 
2) Display “you did good job” in LCD by left shifting from right. 
