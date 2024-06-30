# monitor.py

import psutil
import time
import GPUtil
import argparse

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_gpu_usage():
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
