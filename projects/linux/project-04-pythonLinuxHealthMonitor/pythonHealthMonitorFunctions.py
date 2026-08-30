#!/usr/bin/env python3

############################################################
# Linux Health Monitor Script in Python with functions
# Author: Dharshan
# Version: 1.2
############################################################

import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        return None

computer_name = run_command("hostname")
current_user = run_command("whoami")
current_time = run_command("date")
kernel_version = run_command("uname -r")
cpu_usage = run_command("top -bn 1 | awk '/Cpu/ {print 100 - $8}'")
ram_usage = run_command("free -h | awk '/Mem/'")
ram_split = ram_usage.split()
ram_total = ram_split[1]
current_ram_usage = ram_split[2]
disk_usage = run_command("df -h")
top_5_process = run_command("ps aux --sort=-%cpu | head -6")


print("=" * 120)
print("Linux Server Health Report")
print("=" * 120)

print(f"Hostname       : {computer_name}")
print(f"Username       : {current_user}")
print(f"Current Time   : {current_time}")
print(f"Kernel Version : {kernel_version}")
print(f"CPU Usage      : {cpu_usage}%")
print(f"RAM Usage      : {current_ram_usage}/{ram_total}")

print("=" * 120)
print("Disk Usage")
print(disk_usage)

print("=" * 120)
print("Top 5 Processes")
print(top_5_process)

print("=" * 120)
