#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: internal_temperature_sensor.py
Author: Manuel Caballero
Date: 04/July/2026
Version: 04/July/2026 The ORIGIN
Description: 
    This script demonstrates how to read the (CPU) internal temperature sensor.
	
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

def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        temp_data = int(f.read())
    return temp_data


def main():
    while True:
        try:
            temp = get_cpu_temp() / 1000.0
            print("CPU Temperature:", temp, "°C")
            time.sleep(1)

        except FileNotFoundError:
            print("Temperature sensor file not found.")
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break


if __name__ == "__main__":
    main()