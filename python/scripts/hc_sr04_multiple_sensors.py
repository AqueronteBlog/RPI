#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hc_sr04_multiple_sensors.py
Author: Manuel Caballero
Date: 02/February/2026
Version: 02/February/2026 The ORIGIN
Description: 
    This script demonstrates how to use an external driver for the HC-SR04 ultrasonic sensor.
    Three different ultrasonic sensors are used.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, time, hc_sr04
"""
import RPi.GPIO as GPIO
import time
from hc_sr04 import ultrasonic


def main():
    # Initialize the sensors
    sensor1 = ultrasonic(trig_pin=24, echo_pin=23)
    sensor2 = ultrasonic(trig_pin=21, echo_pin=20)
    sensor3 = ultrasonic(trig_pin=6, echo_pin=5)

    try:
        while True:                        
            pulse_duration1, distance1 = sensor1.measure_distance()
            time.sleep(0.06)
            pulse_duration2, distance2 = sensor2.measure_distance()
            time.sleep(0.06)
            pulse_duration3, distance3 = sensor3.measure_distance()

            print(f"Ultrasonic 1: Pulse duration: {pulse_duration1:.2f} us | Distance: {distance1:.2f} cm\n"
                  f"Ultrasonic 2: Pulse duration: {pulse_duration2:.2f} us | Distance: {distance2:.2f} cm\n"
                  f"Ultrasonic 3: Pulse duration: {pulse_duration3:.2f} us | Distance: {distance3:.2f} cm\n")
            time.sleep(1)  # Wait for 1 second before the next measurement

    except KeyboardInterrupt:
        print("Measurement stopped by user")

    finally:
        # Cleanup GPIO resources
        GPIO.cleanup()


if __name__ == "__main__":
    main()