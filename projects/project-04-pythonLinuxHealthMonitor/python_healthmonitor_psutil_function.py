#########################################################
# Linux Server Health Report Script with psutil function
# Author: Sivadharshan
# Version: 2.2
#########################################################

import psutil
import time
import datetime
import socket

def main():
    system = get_system_info()
    cpu = get_cpu_info()
    memory = get_mem_info()
    return system, cpu, memory

def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)
def bytes_to_mb(value):
    return round(value / (1024 ** 2), 2)

print("="*60)
print("                  LINUX SERVER HEALTH REPORT")
print("="*60)

def get_system_info():
    print("\nSystem")
    print("------")
    hostname = socket.gethostname()
    boottime = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.fromtimestamp(time.time() - psutil.boot_time())
    print(f"Hostname:   {hostname}")
    print(f"Boottime:   {boottime.strftime("%H:%M:%S")}")
    print(f"Uptime: {uptime.strftime("%H:%M:%S")}")
    return hostname, boottime, uptime

def get_cpu_info():
    print("\nCPU")
    print("---")
    cpu_usage = psutil.cpu_percent(interval=0.1)
    cpu_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
    print(f"CPU Usage:  {cpu_usage}%")
    print(f"Physical Cores: {cpu_cores}")
    print(f"Logical Cores:  {logical_cores}")
    print(f"Per CPU Usage:  {per_cpu}")
    return cpu_usage, cpu_cores, logical_cores, per_cpu

def get_mem_info():
    print("\nMemory")
    print("------")
    memory = psutil.virtual_memory()
    total = memory.total
    usage = memory.used
    available = memory.available
    mem_percent = memory.percent
    print(f"Total Memory:   {bytes_to_gb(total)}GB")
    print(f"Used Memory:    {bytes_to_mb(usage)}GB")
    print(f"Available Memory:   {bytes_to_mb(available)}MB")
    print(f"Memory Used Percent:    {mem_percent}%")
    return memory, total, usage, available, mem_percent

main()