#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: gpio_in_polling_edge.py
Author: Manuel Caballero
Date: 13/June/2025
Version: 13/June/2025 The ORIGIN
Description: 
    This script demonstrates how to change the state of an LED by a button.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
        - YouTube: https://www.youtube.com/user/AqueronteBlog
        - X:       https://twitter.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO (rpi-lgpio), time
"""
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED1 = 23
PUSH_BUTTON = 22

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led1_state = GPIO.LOW

while True:
    GPIO.wait_for_edge(PUSH_BUTTON, GPIO.FALLING, bouncetime=200)
    
    led1_state = ~led1_state
    GPIO.output(LED1, led1_state)