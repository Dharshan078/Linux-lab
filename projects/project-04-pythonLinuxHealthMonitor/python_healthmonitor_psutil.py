#################################################
# Linux Server Health Report Script with psutil
# Author: Sivadharshan
# Version: 1.2
#################################################

import psutil
import time

print(f"Overall CPU Usage       :{psutil.cpu_percent(interval=1)}%")
print(f"Overall per CPU Count   :{psutil.cpu_count(logical=False)}")
print(f"Per CPU Usage           :{psutil.cpu_percent(interval=1, percpu=True)}")

memory = psutil.virtual_memory()

def bytes_to_gb(bytes):
    return round((bytes / 1000000000), 2)

print(f"Total Memory            : {bytes_to_gb(memory.total)} GB")
print(f"Available Memory        : {bytes_to_gb(memory.available)} GB")
print(f"Used Memory             : {bytes_to_gb(memory.used)} GB")
print(f"Memory Used Percent     : {(memory.percent)}%")

disk = psutil.disk_usage("/")
print(f"Total Disk              : {bytes_to_gb(disk.total)} GB")
print(f"Total Disk Usage        : {bytes_to_gb(disk.used)} GB")
print(f"Total Available Space   : {bytes_to_gb(disk.free)} GB")
print(f"Disk Used Percentage    : {disk.percent} %")

for partitions in psutil.disk_partitions():
    print(f"Partiton Device         : {partitions.device}")
    print(f"Mountpoint              : {partitions.mountpoint}")
    print(f"Filesystem              : {partitions.fstype}")

def bytes_to_mb(bytes):
    return round((bytes/1000000),2)

network = psutil.net_io_counters()
print(f"Bytes sent              : {network.bytes_sent} | {bytes_to_mb(network.bytes_sent)} MB")
print(f"Bytes received          : {network.bytes_recv} | {bytes_to_mb(network.bytes_recv)} MB")
print(f"Packets Sent            : {network.packets_sent}")
print(f"Packets Receieved       : {network.packets_recv}")
print(f"Drop                    : IN = {network.dropin} | OUT = {network.dropout}")
print(f"Error                   : IN = {network.errin} | OUT = {network.errout}")

interfaces = psutil.net_if_addrs()

for interface, addresses in interfaces.items():
    print("\nInterface:", interface)
    for address in addresses:
        print(" Address:", address.address)

for process in psutil.process_iter():
    print(process.pid, process.name(), process.status())

boot_time = psutil.boot_time()
print(f"Uptime: {boot_time}")

