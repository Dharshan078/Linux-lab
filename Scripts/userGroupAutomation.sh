#!/bin/bash

##########################################
# Linux User Group Automation Script
# Author: Dharshan
# Version: 1.0
##########################################

while true
do

    read -p "Enter username: " username

    if id "$username" &>/dev/null; then
        echo "User '$username' exists."
    else
        sudo useradd -m "$username"
        echo "User '$username' has been created."
        break
    fi
done