#################################################
# Linux Server Health Report Script with psutil
# Author: Sivadharshan
# Version: 2.0
#################################################

#imports
import psutil
import datetime
import socket
import time

#functions
def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)
def bytes_to_mb(value):
    return round(value / (1024 ** 2), 2)

#variables
hostname = socket.gethostname()
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
netinterface = psutil.net_io_counters(pernic=True) # pernic=True -> statistics per network interface.
interfaces = psutil.net_if_addrs()
boot_time = psutil.boot_time()
boot_datetime = datetime.datetime.fromtimestamp(boot_time)
uptime_seconds = time.time() - boot_time
uptime_duration = datetime.timedelta(seconds=uptime_seconds)

#print statements
print("="*60)
print("                  LINUX SERVER HEALTH REPORT")
print("="*60)

print("\nSystem")
print("------")
print(f"Hostname:{hostname}")
print("Boot Time:", boot_datetime)
print("UP Time  :", uptime_duration)

print("\nCPU")
print("---")
print(f"Overall CPU Usage   :{psutil.cpu_percent(interval=1)}%")
print(f"Physical CPU Cores  :{psutil.cpu_count(logical=False)}")
print(f"Logical CPUs        :{psutil.cpu_count(logical=True)}")
print(f"Per CPU Usage       :{psutil.cpu_percent(interval=0.1, percpu=True)}")

print("\nMemory")
print("------")
print(f"Total Memory            : {bytes_to_gb(memory.total)} GB")
print(f"Available Memory        : {bytes_to_gb(memory.available)} GB")
print(f"Used Memory             : {bytes_to_gb(memory.used)} GB")
print(f"Memory Used Percent     : {(memory.percent)}%")

print("\nDisk")
print("----")
print(f"Total Disk              : {bytes_to_gb(disk.total)} GB")
print(f"Total Disk Usage        : {bytes_to_gb(disk.used)} GB")
print(f"Total Available Space   : {bytes_to_gb(disk.free)} GB")
print(f"Disk Used Percentage    : {disk.percent} %")

print("\nPartitions")
print("----------")
for partitions in psutil.disk_partitions():
    print(f"Partiton Device         : {partitions.device}")
    print(f"Mountpoint              : {partitions.mountpoint}")
    print(f"Filesystem              : {partitions.fstype}")

print("\nNetwork")
print("-------")
for interface, stats in netinterface.items():
    print(interface)
    print(" Sent                     :", bytes_to_mb(stats.bytes_sent),"MB")
    print(" Received                 :", bytes_to_mb(stats.bytes_recv),"MB")
    print(f" Packets Sent            : {stats.packets_sent}")
    print(f" Packets Receieved       : {stats.packets_recv}")
    print(f" Drop                    : IN = {stats.dropin} | OUT = {stats.dropout}")
    print(f" Error                   : IN = {stats.errin} | OUT = {stats.errout}")

print("\nNetwork Adresses")
print("---------------")
for interface, addresses in interfaces.items():
    print("Interface:", interface)
    for address in addresses:
        print(" Address:", address.address)

print("\nTop Process")
print("-----------")
processes = []
for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
    processes.append(process.info)
processes.sort(key=lambda cpu: cpu['cpu_percent'], reverse=True)
for process in processes[:5]:
    print(process)



