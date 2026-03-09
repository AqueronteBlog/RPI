#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hc_sr04.py
Author: Manuel Caballero
Date: 02/February/2026
Version: 02/February/2026 The ORIGIN
Description: 
    A Python driver for the HC-SR04 Ultrasonic sensor.
	
    Follow me!: 
    - GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, time
"""
import RPi.GPIO as GPIO
import time

__version__ = '0.1.0'
__author__ = 'Aqueronteblog'
__license__ = "MIT License"

class ultrasonic:
    """
    Driver to use the untrasonic sensor HC-SR04.
    The sensor range is between 2cm and 4m.

    This is a blocking driver! Timeouts are not implemented!

    """
    def __init__(self, trig_pin=24, echo_pin=23):
        """Initialize the ultrasonic sensor with the specified TRIG and ECHO pins."""
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)                  # Use Broadcom pin numbering
        GPIO.setup(self.trig_pin, GPIO.OUT)     # TRIG pin as output
        GPIO.setup(self.echo_pin, GPIO.IN)      # ECHO pin as input
        GPIO.output(self.trig_pin, GPIO.LOW)    # Ensure TRIG is LOW initially
        time.sleep(0.1)                         # Give some time to settle

    def measure_distance(self):
        """Trigger the ultrasonic sensor and measure distance."""
        # Ensure TRIG is LOW to reset before starting
        GPIO.output(self.trig_pin, GPIO.LOW)
        time.sleep(0.1)

        # Send the trigger pulse
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(0.00001)  # 10 microseconds
        GPIO.output(self.trig_pin, GPIO.LOW)

        # Wait for the ECHO pin to go HIGH, indicating the pulse was reflected. This is a blocking command, use timeouts to avoid blocking issues!
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()

        # Wait for the ECHO pin to go LOW, indicating the pulse has returned. This is a blocking command, use timeouts to avoid blocking issues!
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_end = time.time()

        # Calculate pulse duration in microseconds
        pulse_duration = (pulse_end - pulse_start) * 1000000.0  # Convert seconds to microseconds

        # Calculate distance in centimeters
        distance = pulse_duration * 0.017  # Speed of sound = 340 m/s, so 0.034 cm/us (distance = pulse_duration * speed_of_sound / 2)

        return pulse_duration, distance

    def cleanup(self):
        """Cleanup the GPIO pins when done."""
        GPIO.cleanup()