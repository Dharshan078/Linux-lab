#!/bin/bash

##########################################
# Linux User Group Automation Script
# Author: Dharshan
# Version: 1.1
##########################################

if [[ "$EUID" -ne 0 ]]; then
    echo "This script must be run as root. Please run with sudo ./userGroupAutomation.sh"
    exit 1
fi 

while true
do

    read -p "Enter username: " username

    if id "$username" &>/dev/null; then
        echo "User '$username' exists."
    else
        useradd -m "$username"
        passwd "$username"
        echo "======================================================"
        echo "User Created Successfully"
        echo "======================================================"
        echo ""
        echo "Username: $username"
        echo "Home    : /home/$username"
        echo ""
        echo "======================================================"
        break
    fi
done
