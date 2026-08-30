#!/usr/bin/env python3

############################################################
# Linux User Group Automation Script in Python
# Author: Dharshan
# Version: 1.0
############################################################

import subprocess

username = input("Enterusername : ")

while True:
    if id == username:
        print("This user is already exist")
    else:
        createuser = subprocess.run(
            ["useradd", username],
            capture_output=True,
            text=True
        )
        print("User Successfully created: ", createuser.stdout)
        break



