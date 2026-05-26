"""
Filename: tm1637_driver.py
Author:     Manuel Caballero
Date:       26/May/2026
Version:    26/May/2026 The ORIGIN
Description: 
    This script demonstrates how to use the TM1637 driver.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, time, tm1637
"""
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from tm1637 import tm1637

# main
def main():
    display = tm1637(clk=24, dio=23)

    display.display([0, 0, 0, 0])

    for i in range(4):
        display.set_display(on=False)
        time.sleep(0.5)
        display.set_display(on=True)
        time.sleep(0.5)

    display.display([1, 2, 3, 4])
    time.sleep(1)

    display.display([5, 6, 7, 8])
    time.sleep(1)

    try:
        i = 0
        while True:
            display.set_brightness(level=i)
            time.sleep(1)
            if i <= 7:
                i = i + 1
            else:
                i = 0


    except KeyboardInterrupt:
        display.cleanup()



if __name__ == "__main__":
    main()