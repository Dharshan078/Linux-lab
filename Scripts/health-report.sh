#!/bin/bash

#################################################
# Linux Server Health Report Script
# Author: Sivadharshan
# Version: 1.2
#################################################

ComputerName=$(hostname)
CurrentUser=$(whoami)
CurrentDate=$(date)
KernelName=$(uname -r)
CPUUsage=$(top -bn 1 | awk '/Cpu/ {print 100 - $8}')
RAMUsage=$(free -h | awk '/Mem/ {print $3 "/" $2}')
DiskUsage=$(df -h)
Top5Processes=$(ps aux --sort=-%cpu | head -6)

echo ==========================
echo Linux Server Health Report 
echo ==========================
echo "Hostname               : $ComputerName"
echo "Current Logged In User : $CurrentUser"
echo "Time                   : $CurrentDate"
echo "Kernel Version         : $KernelName"
echo "Current CPU Usage      : $CPUUsage%"
echo "Current RAM Usage      : $RAMUsage"
echo "Disk Usage             : "
echo "$DiskUsage"
echo "Top 5 Processes        : "
echo "$Top5Processes"
echo ==========================