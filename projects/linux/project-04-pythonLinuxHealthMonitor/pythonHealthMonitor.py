#!/usr/bin/env python3

############################################################
# Linux Health Monitor Script in Python
# Author: Dharshan
# Version: 1.1
############################################################

# Things to print Hostname, Username, Time, Kernel version, CPU Usage, RAM Usage, Disk Usage, Top 5 process

import subprocess

hostname = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

username = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True
)

date = subprocess.run(
    ["date"],
    capture_output=True,
    text=True
)

kernelversion = subprocess.run(
    ["uname", "-r"],
    capture_output=True,
    text=True
)

cpuUsage = subprocess.run(
    "top -bn1 | grep 'Cpu' | awk '{print 100 - $8}'",
    shell=True,
    capture_output=True,
    text=True
)

ramUsage = subprocess.run(
    "free -h | grep 'Mem' | awk '{print $3,$2}'",
    shell=True,
    capture_output=True,
    text=True,
)
ramOutput = ramUsage.stdout.strip()
ramValues = ramOutput.split()
ramUsed = ramValues[0]
ramTotal = ramValues[1]

diskUsage = subprocess.run(
    "df -h",
    shell=True,
    capture_output=True,
    text=True
)

Top5Process = subprocess.run(
    "ps aux --sort=-%cpu | head -6",
    shell=True,
    capture_output=True,
    text=True
)


print("Hostname: ",hostname.stdout)
print("Current logged in Username: ", username.stdout)
print("Current Time: ", date.stdout)
print("Kernel Version: ", kernelversion.stdout)
print(f"Cpu Usage: {cpuUsage.stdout.strip()}%")
print(f"Ram Utilization: {ramUsed}\nRam Overall: {ramTotal}")
print(f"Disk Usage: \n{diskUsage.stdout}")
print(f"Top 5 Process \n {Top5Process.stdout}")
