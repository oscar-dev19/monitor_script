# monitor.py

import psutil
import time
import GPUtil
import argparse
import sys
from datetime import datetime

def get_cpu_usage():
    """
    Returns the current CPU usage as a percentage.

    This function uses the psutil library to get the current CPU usage. It waits for 1 second before returning the usage to ensure an accurate reading.

    Returns:
        float: The current CPU usage as a percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """
    Returns the current memory usage as a percentage.

    This function uses the psutil library to get the current memory usage. It returns the percentage of used memory.

    Returns:
        float: The current memory usage as a percentage.
    """
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_gpu_usage():
    """
    Returns a list of dictionaries containing information about each GPU's usage.

    This function uses the GPUtil library to get the current usage of each GPU. It returns a list of dictionaries, each containing the GPU's ID, name, load percentage, and memory utilization percentage.

    Returns:
        list: A list of dictionaries, each containing GPU information.
    """
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            'id': gpu.id,
            'name': gpu.name,
            'load': gpu.load * 100,
            'memory_util': gpu.memoryUtil * 100
        })
    return gpu_info

def monitor_system(interval):
    """
    Continuously monitors and prints the system's CPU, memory, and GPU usage at a specified interval, as well as logs the stats to a file if the log argument is passed.

    This function uses a loop to continuously monitor the system's resource utilization. It prints the CPU usage, memory usage, and GPU usage (if available) at the specified interval. If GPUs are not available or GPUtil is not installed, it prints a message indicating so. Additionally, if the log argument is passed, it logs the stats to the specified file.

    Parameters:
        interval (int): The time in seconds between each monitoring output.

    Returns:
        None
    """
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        gpu_usage = None
        try:
            gpu_usage = get_gpu_usage()
        except:
            print("GPUs not available or GPUtil not installed.")
        
        output = "CPU Usage: {}%\nMemory Usage: {}%".format(cpu_usage, memory_usage)
        if gpu_usage:
            for gpu in gpu_usage:
                output += "\nGPU ID: {}\nGPU Name: {}\nGPU Load: {}%\nGPU Memory Utilization: {}%".format(gpu['id'], gpu['name'], gpu['load'], gpu['memory_util'])
        output += "\n" + "-" * 20
        
        print(output)  # Always print the output to the console
        
        if args.log:
            with open(args.log, 'a') as f:
                f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + output + "\n")  # Log the output to the file if log argument is passed, including the date
        time.sleep(interval)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor system resource utilization.")
    parser.add_argument("--interval", type=int, default=5, help="Interval (in seconds) between each monitoring output.")
    parser.add_argument("--log", type=str, default=None, help="Optional log file.")
    args = parser.parse_args()
    
    if args.log:
        with open(args.log, 'w') as f:
            sys.stdout = f
            monitor_system(args.interval)
    else:
        monitor_system(args.interval)