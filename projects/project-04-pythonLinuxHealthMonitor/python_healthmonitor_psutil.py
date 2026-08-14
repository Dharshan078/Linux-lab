#################################################
# Linux Server Health Report Script with psutil
# Author: Sivadharshan
# Version: 1.2
#################################################

import psutil

print(f"Overall CPU Usage      :{psutil.cpu_percent(interval=1)}%")
print(f"Overall per CPU Count  :{psutil.cpu_count(logical=False)}")
print(f"Per CPU Usage          :{psutil.cpu_percent(interval=1, percpu=True)}")

memory = psutil.virtual_memory()
print(memory.total)
print(memory.used)
print(memory.available)
print(memory.percent)
print(memory)
