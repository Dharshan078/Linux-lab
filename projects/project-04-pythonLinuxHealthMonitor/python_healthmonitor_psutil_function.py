#########################################################
# Linux Server Health Report Script with psutil function
# Author: Sivadharshan
# Version: 2.2
#########################################################

import psutil
import time
import datetime
import socket

def sectotime(x):
    x = ((x%86400) / 3600)
    return x

def main():
    system = get_system_info()
    return system

def get_system_info():
    hostname = print(f"Hostname:    {socket.gethostname()}")
    boottime = print(f"Boottime:    {psutil.boot_time()}")
    return hostname, sectotime(boottime)

def get_cpu_info():

    return

main()