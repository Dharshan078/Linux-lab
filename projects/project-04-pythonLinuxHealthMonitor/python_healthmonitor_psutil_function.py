#########################################################
# Linux Server Health Report Script with psutil function
# Author: Sivadharshan
# Version: 2.2
#########################################################

import psutil
import time
import datetime
import socket

def get_system_info():
    hostname = socket.gethostname()
    boottime = psutil.boot_time()
    return hostname, boottime

def get_cpu_info():
    return

print(get_system_info())