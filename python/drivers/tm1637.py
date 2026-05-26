#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: tm1637.py
Author: Manuel Caballero
Date: 26/May/2026
Version: 26/May/2026 The ORIGIN
Description: 
    A Python driver for the TM1637 LED Drive Control Special Circuit sensor.
	
    Follow me!: 
    - GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: RPi.GPIO
"""
import RPi.GPIO as GPIO

__version__ = '0.1.0'
__author__ = 'Aqueronteblog'
__license__ = "MIT License"

class tm1637:
    """
    Driver to use the LED Drive Control Special Circuit: TM1637.

    """
    def __init__(self, clk, dio):
        """Initialize the TM1637 device with the specified CLK and DIO pins."""
        self.clk = clk
        self.dio = dio

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.OUT)
        GPIO.setup(self.dio, GPIO.OUT)

        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.HIGH)

        # Display state
        self.brightness = 7       # 0–7
        self.display_on = True

        # Digit to segment map (0–9)
        self.digits = [
            0x3f, 0x06, 0x5b, 0x4f,
            0x66, 0x6d, 0x7d, 0x07,
            0x7f, 0x6f
        ]

    def _start(self):
        """Initialize the TM1637 communication protocol."""
        GPIO.output(self.dio, GPIO.HIGH)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.LOW)
        GPIO.output(self.clk, GPIO.LOW)

    def _stop(self):
        """Stop the TM1637 communication protocol."""
        GPIO.output(self.clk, GPIO.LOW)
        GPIO.output(self.dio, GPIO.LOW)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.HIGH)

    def _write_byte(self, byte):
        """Send sata to the TM1637 communication protocol."""
        for i in range(8):
            GPIO.output(self.clk, GPIO.LOW)
            GPIO.output(self.dio, (byte >> i) & 0x01)
            GPIO.output(self.clk, GPIO.HIGH)

        # ACK bit (ignore result)
        GPIO.output(self.clk, GPIO.LOW)
        GPIO.setup(self.dio, GPIO.IN)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.setup(self.dio, GPIO.OUT)

    def set_display(self, on=True):
        """
        Turn display ON or OFF.
        """

        self.display_on = on
        self._update_display_control()

    def set_brightness(self, level):
        """
        Set brightness level (0–7).
        """

        level = max(0, min(7, level))
        self.brightness = level

        self._update_display_control()

    def _update_display_control(self):
        """
        Send display control command.
        """

        self._start()

        command = 0x88 if self.display_on else 0x80
        command |= self.brightness

        self._write_byte(command)

        self._stop()

    def display(self, numbers):
        """
        Display data. Numbers: list of 4 digits (0–9)
        """
        segments = [self.digits[n] for n in numbers]

        # Command 1: automatic address increment
        self._start()
        self._write_byte(0x40)
        self._stop()

        # Command 2: set starting address
        self._start()
        self._write_byte(0xC0)

        for seg in segments:
            self._write_byte(seg)

        self._stop()

        # Command 3: display control (brightness 0–7)
        self._start()
        self._write_byte(0x88 | 0x07)  # display ON, max brightness
        self._stop()

    def cleanup(self):
        """Cleanup the GPIO pins when done."""
        GPIO.cleanup()