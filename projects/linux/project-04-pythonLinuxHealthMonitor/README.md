# Linux Server Health Monitoring

## Overview

A python based Linux health server monitoring script using psutil supported on windows too

## Output
![Linux Server Health Report Output 1](<Output Screenshots/Linux Server Health Report Output 1.png>)
![Linux Server Health Report Output 2](<Output Screenshots/Linux Server Health Report Output 2.png>)

## Features

### System Info
    - Hostname
    - Boottime
    - Uptime

### CPU
    - CPU Utilization
    - CPU Core details

### Memory
    - Memory Usage

### Disk
    - Disk Usage

### Partitions
    - Partivion Device
    - Mount Point
    - File System

### Network
    - Network interface utilization details
    - Network Interface details with IP and MAC Address

### Process
    - Top 5 process details

### Logging
    - Logging added to know the status

## Technologies
    - Python 3
    - psutil
    - Linux

## How to run
    ```bash python3 python_healthmonitor_psutil_function.py```

## Version Details
    - v1 -> Used Subprocess to run linux command directly from python
    - v2 -> Used psutil for multi OS Support
    - v2.2 -> Used function better 
    - v2.3 -> Used return better along with functions
    - v2.4 -> Added logging to know the status of the program