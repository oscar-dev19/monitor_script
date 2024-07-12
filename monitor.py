# monitor.py

import psutil
import time
import GPUtil
import argparse

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
    Continuously monitors and prints the system's CPU, memory, and GPU usage at a specified interval.

    This function uses a loop to continuously monitor the system's resource utilization. It prints the CPU usage, memory usage, and GPU usage (if available) at the specified interval. If GPUs are not available or GPUtil is not installed, it prints a message indicating so.

    Parameters:
        interval (int): The time in seconds between each monitoring output.

    Returns:
        None
    """
    while True:
        print("CPU Usage: {}%".format(get_cpu_usage()))
        print("Memory Usage: {}%".format(get_memory_usage()))
        
        try:
            gpu_usage = get_gpu_usage()
            if gpu_usage:
                for gpu in gpu_usage:
                    print("GPU ID: {}".format(gpu['id']))
                    print("GPU Name: {}".format(gpu['name']))
                    print("GPU Load: {}%".format(gpu['load']))
                    print("GPU Memory Utilization: {}%".format(gpu['memory_util']))
        except:
            print("GPUs not available or GPUtil not installed.")

        print("-" * 20)
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor system resource utilization.")
    parser.add_argument("--interval", type=int, default=5, help="Interval (in seconds) between each monitoring output.")
    args = parser.parse_args()
    
    monitor_system(args.interval)
