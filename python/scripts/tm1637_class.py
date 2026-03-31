#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: tm1637_class.py
Author:     Manuel Caballero
Date:       31/March/2026
Version:    31/March/2026 The ORIGIN
Description: 
    This script demonstrates how to make a python code for the TM1637 LED drive control special circuit.
	
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

class TM1637:
    def __init__(self, clk, dio):
        self.clk = clk
        self.dio = dio

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.OUT)
        GPIO.setup(self.dio, GPIO.OUT)

        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.HIGH)

        # Digit to segment map (0–9)
        self.digit7seg = [
            0x3F, 0x06, 0x5B, 0x4F,
            0x66, 0x6D, 0x7D, 0x07,
            0x7F, 0x6F
        ]

    def _start(self):
        GPIO.output(self.dio, GPIO.HIGH)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.LOW)
        GPIO.output(self.clk, GPIO.LOW)

    def _stop(self):
        GPIO.output(self.clk, GPIO.LOW)
        GPIO.output(self.dio, GPIO.LOW)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.output(self.dio, GPIO.HIGH)

    def _write_byte(self, byte):
        for i in range(8):
            GPIO.output(self.clk, GPIO.LOW)
            GPIO.output(self.dio, (byte >> i) & 0x01)
            GPIO.output(self.clk, GPIO.HIGH)

        # ACK bit (ignore result)
        GPIO.output(self.clk, GPIO.LOW)
        GPIO.setup(self.dio, GPIO.IN)
        GPIO.output(self.clk, GPIO.HIGH)
        GPIO.setup(self.dio, GPIO.OUT)

    def display(self, numbers):
        """
        numbers: list of 4 digits (0–9)
        """
        segments = [self.digit7seg[n] for n in numbers]

        # Command 1: Automatic address increment
        self._start()
        self._write_byte(0x40)
        self._stop()

        # Command 2: Set starting address and data to be sent
        self._start()
        self._write_byte(0xC0)

        for seg in segments:
            self._write_byte(seg)

        self._stop()

        # Command 3: Display control (brightness 0–7)
        self._start()
        self._write_byte(0x88 | 0x07)  # display ON, max brightness
        self._stop()


def main():
    display = TM1637(clk = 24, dio = 23)

    try:
        while True:
            display.display([1, 2, 3, 4])
            time.sleep(1)

            display.display([5, 6, 7, 8])
            time.sleep(1)

            display.display([0, 9, 0, 9])
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == "__main__":
    main()