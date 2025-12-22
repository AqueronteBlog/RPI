#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hc_sr04_class.py
Author: Manuel Caballero
Date: 22/December/2025
Version: 22/December/2025 The ORIGIN
Description: 
    This script demonstrates how to wrap the python code for the HC-SR04 ultrasonic sensor.
	
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

# PIN Configuration (BCM pins)
TRIG = 24
ECHO = 23


class hc_sr04:
    def __init__(self, trig_pin = 24, echo_pin = 23):
        """Initialize the ultrasonic sensor with the specified TRIG and ECHO pins."""
        self.trig_pin   =   trig_pin
        self.echo_pin   =   echo_pin

        # Setup GPIO
        GPIO.cleanup()              # Reset GPIO
        GPIO.setmode(GPIO.BCM)      # Use Broadcom pin numbering
        GPIO.setup(TRIG, GPIO.OUT)  # TRIG pin as output pin
        GPIO.setup(ECHO, GPIO.IN)   # ECHO pin as input pin
        GPIO.output(TRIG, GPIO.LOW) # HC-SR04 protocol reset

    def measure_distance(self):
        """Trigger the ultrasonic sensor and measure distance."""
        # New measurement 
        GPIO.output(self.trig_pin, GPIO.LOW)     # HC-SR04 protocol reset
        time.sleep(0.1)
        GPIO.output(self.trig_pin, GPIO.HIGH)    # HC-SR04. TRIG
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, GPIO.LOW)  

        # ECHO
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()   # Record the time when the pulse starts   

        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_end = time.time()     # Record the time when the pulse ends

        # Calculate distance in cm
        pulse_duration = (pulse_end - pulse_start)*1000000.0    # from s to us
        distance = pulse_duration*(17.0/1000.0)                 # Speed of sound = 340 m/s, Range = Echo(us)*velocity/2
                                                                # Range(cm) = Echo(us)*(0.034/2)cm/us = Echo(us)*0.017cm/us = Echo(us)*(17/1000)cm/us

        return  pulse_duration, distance

    def cleanup (self):
        """Cleanup the GPIO pins when done."""
        GPIO.cleanup()


# main
def main():
   # Init the HC-SR04
   sensor = hc_sr04 (trig_pin = TRIG, echo_pin = ECHO)
   
   try:
    while True:
        pulse_duration, distance = sensor.measure_distance()
        print(f"Pulse duration: {pulse_duration:.2f} us | Distance: {distance:.2f} cm")
        time.sleep(1)           # Wait for 1 second bfore the next measurement
   except KeyboardInterrupt:
        print("Measurement stopped by user")
        sensor.cleanup()              # Reset GPIO

if __name__ == "__main__":
    main()