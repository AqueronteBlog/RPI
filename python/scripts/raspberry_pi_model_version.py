"""
Filename:   raspberry_pi_model_version.py
Author:     Manuel Caballero
Date:       13/September/2026
Version:    13/September/2026 The ORIGIN
Description: 
    This script shows how to get the Raspberry Pi version.
	
    Follow me!: 
	- GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: time
"""
#!/usr/bin/env python3
import time


# def: It gets the Raspberry Pi model version
def get_raspberry_pi_model():
    with open("/proc/device-tree/model", "r") as file:
        return file.read().strip("\x00\n")


# main
def main():
    try:
        while True:
            model = get_raspberry_pi_model()    # Get RPI model

            print("Raspberry Pi model:", model)
            time.sleep(1)  # Wait for 1 second before the next measurement

    except KeyboardInterrupt:
        print("Script stopped by user")


if __name__ == "__main__":
    main()