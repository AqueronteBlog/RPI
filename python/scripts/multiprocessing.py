#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: multiprocessing.py
Author: Manuel Caballero
Date: 02/November/2025
Version: 02/November/2025 The ORIGIN
Description: 
    This script demonstrates how to work with multiprocessing. Two processess are configured to make two LEDs blink.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://twitter.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, threading, signal, time
"""
import RPi.GPIO as GPIO
import time
from multiprocessing import Process

# LED pin configurations
LED1_PIN = 23  # GPIO23 for first LED
LED2_PIN = 24  # GPIO24 for second LED

# multiprocess funtion to for LED blinking
def blink_led(pin, interval):
    """Process function to control individual LED"""
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(interval)
    except KeyboardInterrupt:
        GPIO.cleanup()


# main
if __name__ == "__main__":
    # Configure GPIOs
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED1_PIN, GPIO.OUT)
    GPIO.setup(LED2_PIN, GPIO.OUT)
    
    # Configure the multiprocesses for cleanup when the script ends
    processes = []

    try:
        # Create processes for each LED
        led1_process = Process(target=blink_led, args=(LED1_PIN, 0.5))
        led2_process = Process(target=blink_led, args=(LED2_PIN, 1.0))

        # Store processes for cleanup
        processes.extend([led1_process, led2_process])

        # Start processes
        led1_process.start()
        led2_process.start()

        # Keep main process running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Terminate all processes
        for process in processes:
            process.terminate()
            process.join()
        GPIO.cleanup()
        print("\nProgram ended by user")