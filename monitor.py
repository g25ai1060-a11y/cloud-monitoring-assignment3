import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    print("Current CPU Usage:", cpu, "%")
    time.sleep(1)
