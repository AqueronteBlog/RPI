#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: threads.py
Author: Manuel Caballero
Date: 18/October/2025
Version: 18/October/2025 The ORIGIN
Description: 
    This script demonstrates how to work with threads. Two threads are configured to make two LEDs blink.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://twitter.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO, threading, signal, time
"""
import threading
import time
import signal
import RPi.GPIO as GPIO

# PIN Configuration (BCM pins and intervals)
LED1_PIN = 23
LED2_PIN = 24

LED1_INTERVAL = 0.5
LED2_INTERVAL = 1


# def: Thread1 and Thread2
def blink_loop (pin, interval, stop_evt):
    GPIO.setup (pin, GPIO.OUT)
    GPIO.output (pin, False)
    state = False

    try:
        while not stop_evt.is_set():
            state = not state
            GPIO.output (pin, state)
            if stop_evt.wait(interval):
                break
    finally:
        GPIO.output (pin, False)


# Force stopping events for each thread
def _handle_sigint(signum, frame):
    _stop_evt1.set()
    _stop_evt2.set()


# Independent stop events for each thread
_stop_evt1 = threading.Event()
_stop_evt2 = threading.Event()

# Independent stop events for each thread by signal
signal.signal(signal.SIGINT, _handle_sigint)
signal.signal(signal.SIGTERM, _handle_sigint)


# def: main
def main():
    GPIO.setmode(GPIO.BCM)

    thread1 = threading.Thread(target=blink_loop, args=(LED1_PIN, LED1_INTERVAL, _stop_evt1), daemon=True)
    thread2 = threading.Thread(target=blink_loop, args=(LED2_PIN, LED2_INTERVAL, _stop_evt2), daemon=True)

    thread1.start()
    thread2.start()

    try:
        print(f"LEDs: {LED1_PIN}@{LED1_INTERVAL}s, {LED2_PIN}@{LED2_INTERVAL}s")
        
        while True:
            time.sleep(10)
    
    except KeyboardInterrupt:
        _stop_evt1.set()
        _stop_evt2.set()
    
    finally:
        thread1.join (timeout = 1.0)
        thread2.join (timeout = 1.0)
        
        GPIO.cleanup((LED1_PIN, LED2_PIN))

# main
if __name__ == "__main__":
    main()