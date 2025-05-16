#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: hello_world.py
Author: Manuel Caballero
Date: 16/May/2025
Version: 16/May/2025 The ORIGIN
Description: 
    This script demonstrates how to blink an LED every one second.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
        - YouTube: https://www.youtube.com/user/AqueronteBlog
        - X:       https://twitter.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, time
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED1 = 23   # LED pin

GPIO.setup(LED1, GPIO.OUT)

while True:
    GPIO.output(LED1, GPIO.HIGH)    # LED on
    time.sleep(1)
    GPIO.output(LED1, GPIO.LOW)     # LED off
    time.sleep(1)