#########################################################
# Linux Server Health Report Script with psutil function
# Author: Sivadharshan
# Version: 2.4
#########################################################

import psutil
import time
import datetime
import socket
import logging

logging.basicConfig(
    filename="health_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    logging.info("Linux health monitoring started")
    print("="*60)
    print("                  LINUX SERVER HEALTH REPORT")
    print("="*60)

    system = get_system_info()
    cpu = get_cpu_info()
    memory = get_mem_info()
    disks = get_disk_info()
    partitions = get_partition_info()
    netaddress = get_net_addr()
    netinfo = get_net_info()
    top_process = get_top_process()

    print("\nSystem")
    print("------")
    print(f"Hostname:   {system[0]}")
    print(f"Boottime:   {system[1].strftime("%H:%M")}")
    print(f"Uptime: {system[2]}")

    print("\nCPU")
    print("---")
    print(f"CPU Usage       :{cpu[0]}%")
    print(f"Physical Cores  :{cpu[1]}")
    print(f"Logical Cores   :{cpu[2]}")
    print(f"Per CPU Usage   :{cpu[3]}")

    print("\nMemory")
    print("------")
    print(f"Total Memory: {bytes_to_gb(memory.total)} GB")
    print(f"Used Memory: {bytes_to_mb(memory.used)} MB")
    print(f"Available Memory: {bytes_to_mb(memory.available)} MB")
    print(f"Memory Used Percent: {memory.percent}%")

    print("\nDisk")
    print("----")
    if disks is None:
        print("Disk information unavailable.")
    else:
        disktotal = disks.total
        diskused = disks.used
        diskfree = disks.free
        diskpercent = disks.percent
        print(f"Total Disk: {bytes_to_gb(disktotal)}GB")
        print(f"Total Disk Usage: {bytes_to_gb(diskused)}GB")
        print(f"Total Available Space: {bytes_to_mb(diskfree)}MB")
        print(f"Disk Used Percent: {diskpercent}%")


    print("\nPartitions")
    print("----------")
    for partition in partitions:
        print(f"Parition Device:    ", partition.device)
        print(f"Mount Point:    ", partition.mountpoint)
        print(f"FileSystem:     ", partition.fstype)

    print("\nNetwork")
    print("-------")
    for interface, stats in netinfo.items():
        print(interface)
        print(" Sent                     :", bytes_to_mb(stats.bytes_sent),"MB")
        print(" Received                 :", bytes_to_mb(stats.bytes_recv),"MB")
        print(f" Packets Sent            : {stats.packets_sent}")
        print(f" Packets Receieved       : {stats.packets_recv}")
        print(f" Drop                    : IN = {stats.dropin} | OUT = {stats.dropout}")
        print(f" Error                   : IN = {stats.errin} | OUT = {stats.errout}")

    print("\nNetwork Adresses")
    print("---------------")
    for interface, addresses in netaddress.items():
        print("Interface: ", interface)
        for address in addresses:
            print("Address: ", address.address)

    print("\nTop Process")
    print("-----------")
    for process in top_process:
        print(process)

    logging.info("Linux health monitoring completed")

def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)
def bytes_to_mb(value):
    return round(value / (1024 ** 2), 2)


def get_system_info():
    hostname = socket.gethostname()
    boottime = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = datetime.timedelta(seconds=uptime_seconds)
    return hostname, boottime, uptime

def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=0.1)
    cpu_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
    return cpu_usage, cpu_cores, logical_cores, per_cpu

def get_mem_info():
    return psutil.virtual_memory()

def get_disk_info():
    try:
        return psutil.disk_usage("/")
    except OSError:
        logging.exception(f"Unable to retrieve disk information")
        return None


def get_partition_info():
    partitions = []
    for partition in psutil.disk_partitions():
        partitions.append(partition)
    return partitions

def get_net_info():
    return psutil.net_io_counters(pernic=True) 

def get_net_addr():
    return psutil.net_if_addrs()

def get_top_process():
    processes=[]
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        processes.append(process.info)
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    top_processes = processes[:5]
    return top_processes

if __name__ == "__main__":
    main()