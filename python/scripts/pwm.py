#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: pwm.py
Author: Manuel Caballero
Date: 20/June/2026
Version: 20/June/2026 The ORIGIN
Description: 
    This script demonstrates how to generate a PWM signal.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, time
"""
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time


PWM_PIN = 23       # GPIO23 supports hardware PWM
FREQUENCY = 500    # 500 Hz PWM


# main
def main():
    GPIO.setmode(GPIO.BCM)      # Use Broadcom pin numbering

    GPIO.setup(PWM_PIN, GPIO.OUT)

    pwm = GPIO.PWM(PWM_PIN, FREQUENCY)
    pwm.start(0)                # start with 0% duty cycle

    try:
        while True:
            # Fade up
            for duty in range(0, 101, 10):
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.1)

            # Fade down
            for duty in range(100, -1, -10):
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("Script stopped by User")
        pwm.stop()
        GPIO.cleanup()          # Clean up GPIO when exiting


if __name__ == "__main__":
    main()