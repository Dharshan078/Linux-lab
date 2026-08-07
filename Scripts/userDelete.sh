#!/bin/bash

##########################################
# Linux User Deletion Automation Script
# Author: Dharshan
# Version: 1.0
##########################################

if [[ "$EUID" -ne 0 ]]; then
    echo "This script must be run as root. Please run with sudo ./userDelete.sh"
    exit 1
fi

while true
do
    read -p "Enter Username to delete: " username
    
    if id "$username" &>/dev/null; then
        read -p "Do you really want to delete $username (y/n):" confirm
        if [[ $confirm == 'y' || $confirm == 'Y' ]]; then
            userdel -r "$username"
            echo "User $username has been Deleted"
            break
        else
            echo "User Deletion Cancelled"
        fi
    else
        echo "User not exist to delete"
    fi
done