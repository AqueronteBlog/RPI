#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: gpio_in_callback.py
Author: Manuel Caballero
Date: 18/June/2025
Version: 18/June/2025 The ORIGIN
Description: 
    This script demonstrates how to change the state of an LED by a button using a callback.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
        - YouTube: https://www.youtube.com/user/AqueronteBlog
        - X:       https://twitter.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO
"""
import RPi.GPIO as GPIO

# GPIO IN interrupt/callback
def button_callback(channel):
    global led1_state

    if (led1_state == False):
        GPIO.output(LED1, GPIO.HIGH)
        print("LED1 is on")
        led1_state = True
    else:
        GPIO.output(LED1, GPIO.LOW)
        print("LED1 is off")
        led1_state = False


GPIO.setmode(GPIO.BCM)
LED1 = 23
PUSH_BUTTON = 22

led1_state = False

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(PUSH_BUTTON, GPIO.FALLING, callback = button_callback, bouncetime = 200)

message = input("Press enter to quit\n\n")
GPIO.cleanup()