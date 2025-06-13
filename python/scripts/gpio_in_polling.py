#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: gpio_in_polling.py
Author: Manuel Caballero
Date: 01/June/2025
Version: 01/June/2025 The ORIGIN
Description: 
    This script demonstrates how to change the state of an LED by a button.
	
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
LED1 = 23
PUSH_BUTTON = 22

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led1_state = GPIO.LOW

while True:
    if (GPIO.input(PUSH_BUTTON) == GPIO.LOW):
        led1_state = ~led1_state
        GPIO.output(LED1, led1_state)
        time.sleep(0.2)