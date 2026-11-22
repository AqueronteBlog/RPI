"""
Filename:   internal_ram_memory.py
Author:     Manuel Caballero
Date:       22/November/2026
Version:    22/November/2026 The ORIGIN
Description: 
    This script shows how to analyse the internal RAM memory.
	
    Follow me!: 
    - GitHub:  https://github.com/AqueronteBlog
    - YouTube: https://www.youtube.com/user/AqueronteBlog
    - X:       https://x.com/aqueronteblog

License: MIT License
Contact: aqueronteblog@gmail.com
Dependencies: time, datatime
"""
#!/usr/bin/env python3
import time
from datetime import datetime

# Read Linux memory information
def get_ram_info():
    memory_info = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":", 1)
            memory_info[key] = int(value.strip().split()[0])

    # Values are provided in kB
    total_ram = memory_info["MemTotal"]
    free_ram = memory_info["MemFree"]
    available_ram = memory_info["MemAvailable"]

    # Calculate used RAM
    used_ram = total_ram - available_ram

    # Convert kB to MB
    total_mb = total_ram / 1024
    used_mb = used_ram / 1024
    available_mb = available_ram / 1024
    free_mb = free_ram / 1024

    # Calculate usage percentage
    usage_percent = (used_ram / total_ram) * 100

    # Display results
    print("\n" + "=" * 45)
    print("       RASPBERRY PI RAM MONITOR")
    print("=" * 45)

    print("Date/Time      :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Total RAM      : {total_mb:.2f} MB")
    print(f"Used RAM       : {used_mb:.2f} MB")
    print(f"Available RAM  : {available_mb:.2f} MB")
    print(f"Free RAM       : {free_mb:.2f} MB")
    print(f"RAM Usage      : {usage_percent:.2f}%")


# main
def main():
    try:
        while True:
            get_ram_info()
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nRAM monitoring stopped.")


if __name__ == "__main__":
    main()