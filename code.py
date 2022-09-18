import time
import psutil

print("Hello World")
 
 
def display_usage(cpu_usage,mem_usage,bars=50):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar = '▉' * int(cpu_percent*bars) + '-' * (bars - int(cpu_percent*bars))
    mem_percent = (mem_usage/100.0)
 
    mem_bar = '▉' * int(mem_percent*bars) + '-' * (bars - int(mem_percent*bars))
 
    print(f"\r CPU Usage: | |{cpu_bar}| {cpu_usage:.2f}%",end="")
    print(f" Mem Usage: | |{mem_bar}| {mem_usage:.2f}%",end="\r")
 
while True:
 
   print(f'CPU usage is {psutil.cpu_percent()}, Memory usage is {psutil.virtual_memory().percent},30')
   time.sleep(10)
