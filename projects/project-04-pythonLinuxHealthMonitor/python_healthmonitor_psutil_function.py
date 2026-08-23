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
    disk = get_disk_info()
    partition = get_partition_info()
    netaddress = get_net_address()
    top_process = get_top_process()
    return system, cpu, memory, disk, partition, netaddress, top_process

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
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = datetime.timedelta(seconds=uptime_seconds)
    print(f"Hostname:   {hostname}")
    print(f"Boottime:   {boottime.strftime("%H:%M:%S")}")
    print(f"Uptime: {uptime}")
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

def get_disk_info():
    print("\nDisk")
    print("----")
    disk = psutil.disk_usage("/")
    disktotal = disk.total
    diskused = disk.used
    diskfree = disk.free
    diskpercent = disk.percent
    print(f"Total Disk: {bytes_to_gb(disktotal)}GB")
    print(f"Total Disk Usage: {bytes_to_gb(diskused)}GB")
    print(f"Total Available Space: {bytes_to_mb(diskfree)}MB")
    print(f"Disk Used Percent: {diskpercent}%")
    return disk

def get_partition_info():
    print("\nPartitions")
    print("----------")
    for partition in psutil.disk_partitions():
        print(f"Partition Device: {partition.device}")
        print(f"Mount Point: {partition.mountpoint}")
        print(f"Filesystem: {partition.fstype}")
    return partition

def get_net_address():
    print("\nNetwork")
    print("-------")
    net = psutil.net_io_counters(pernic=True)
    for interface, stats in net.items():
        print(interface)
        print(" Sent                     :", bytes_to_mb(stats.bytes_sent),"MB")
        print(" Received                 :", bytes_to_mb(stats.bytes_recv),"MB")
        print(f" Packets Sent            : {stats.packets_sent}")
        print(f" Packets Receieved       : {stats.packets_recv}")
        print(f" Drop                    : IN = {stats.dropin} | OUT = {stats.dropout}")
        print(f" Error                   : IN = {stats.errin} | OUT = {stats.errout}")
    return net

def get_top_process():
    print("\nTop Process")
    print("-----------")
    processes=[]
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        processes.append(process.info)
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    for process in processes[:5]:
        print(process)
    return process

main()