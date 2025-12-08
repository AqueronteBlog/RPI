#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hc_sr04.py
Author: Manuel Caballero
Date: 08/December/2025
Version: 08/December/2025 The ORIGIN
Description: 
    This script demonstrates how to work with the external ultrasonic sensor HC-SR04.
    A new measurement is triggered every second.
	
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

# Configuration (BCM pins)
TRIG = 24               # Trigger pin connected to GPIO 24
ECHO = 23               # Echo pin connected to GPIO 23

def measure_distance():
    # Send a short pulse to trigger the sensor
    GPIO.output(TRIG, GPIO.LOW)     # Ensure the trigger is low before starting
    time.sleep(0.1)                 # Wait a moment for a stable low signal
    GPIO.output(TRIG, GPIO.HIGH)    # Trigger the sensor
    time.sleep(0.00001)             # Keep the trigger high for 10 microseconds
    GPIO.output(TRIG, GPIO.LOW)     # Turn the trigger back to low

    # Wait for the Echo pin to return to HIGH
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()   # Record the time when the pulse starts

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()     # Record the time when the pulse ends

    # Calculate distance in centimeters
    pulse_duration = (pulse_end - pulse_start) * 1000000.0  # from s to us
    distance = pulse_duration * (17.0/ 1000.0)              # Speed of sound is 340 m/s, Range = Echo(us)*velocity/2
                                                            # Range = Echo(us)*(0.034/2)cm/us = Echo(us)*0.017cm/us = Echo(us)*(17/1000)cm/us 

    return pulse_duration, distance

# main
def main():
    GPIO.cleanup()              # Reset GPIO
    GPIO.setmode(GPIO.BCM)      # Use Broadcom pin numbering

    GPIO.setup(TRIG, GPIO.OUT)  # Set the Trigger pin as an output
    GPIO.setup(ECHO, GPIO.IN)   # Set the Echo pin as an input

    GPIO.output(TRIG, GPIO.LOW) # HC-SR04 protocol reset

    try:
        while True:
            pulse_duration, distance = measure_distance()
            print(f"Pulse duration: {pulse_duration:.2f} us | Distance: {distance:.2f} cm")
            time.sleep(1)       # Wait for 1 second before the next measurement
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()          # Clean up GPIO when exiting


if __name__ == "__main__":
    main()