import psutil
import time

def has_gpu():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        return bool(gpus)
    except ImportError:
        return False

def monitor_resources(interval):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        memory_info = psutil.virtual_memory()

        output = f"CPU Usage: {cpu_percent:.2f}% | Memory Usage: {memory_info.percent:.2f}%"

        if has_gpu():
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu_info = gpus[0]
                output += f" | GPU Usage: {gpu_info.load*100:.2f}% | GPU Memory Usage: {gpu_info.memoryUtil*100:.2f}%"
            else:
                output += " | No GPUs available."
        else:
            output += " | No GPU found."

        print(output, end='\r', flush=True)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_resources(interval=5)  # Monitor every 5 seconds

