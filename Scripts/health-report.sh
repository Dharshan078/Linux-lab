#!/bin/bash
#======== Commands and Variable ========
ComputerName=$(hostname)
CurrentUser=$(whoami)
CurrentDate=$(date)
KernelName=$(uname -r)
CPUUsage=$(top -bn 1 | head -5)
RAMUsage=$(free -h)
DIskUsage=$(df -h)
Top5Processes=$(ps aux --sort=-%cpu | head -5)

echo ==========================
echo Linux Server Health Report 
echo ==========================
echo "Hostname               : $ComputerName"
echo "Current Logged In User : $CurrentUser"
echo "Time                   : $CurrentDate"
echo "Kernel Version         : $KernelName"
echo Current CPU Usage:
echo $CPUUsage
echo Current RAM Usage:
echo $RAMUsage
echo Top 5 Processes
echo $Top5Processes