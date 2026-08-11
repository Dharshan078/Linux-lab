#!/usr/bin/env python3

############################################################
# Linux Health Monitor Script in Python
# Author: Dharshan
# Version: 1.0
############################################################

# Things to print Hostname, Username, Time, Kernel version, CPU Usage, RAM Usage, Disk Usage, Top 5 process

import subprocess

hostname = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)
print("Hostname: ",hostname.stdout)

username = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True
)
print("Current logged in Username: ", username.stdout)

date = subprocess.run(
    ["date"],
    capture_output=True,
    text=True
)
print("Current Time: ", date.stdout)

kernelversion = subprocess.run(
    ["uname", "-r"],
    capture_output=True,
    text=True
)
print("Kernel Version: ", kernelversion.stdout)

cpuUsage = subprocess.run(
    ["top","-bn","1","|","awk","'/Cpu/ {print 100 - $8}'"],
    capture_output=True,
    text=True
)
print("CPU Usage: ",cpuUsage.stdout)