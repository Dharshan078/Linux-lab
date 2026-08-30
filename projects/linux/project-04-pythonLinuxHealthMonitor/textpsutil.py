import psutil

print(psutil.cpu_percent(interval=1))

print(psutil.virtual_memory())

print(psutil.disk_usage("/"))

memory = psutil.virtual_memory()

print(memory.total)
print(memory.used)
print(memory.available)
print(memory.percent)