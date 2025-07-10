import os
import time
import psutil
from datetime import datetime

try:
    import GPUtil
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False

class SystemMonitor:
    def __init__(self):
        self.gpu_devices = []
        if GPU_AVAILABLE:
            self.gpu_devices = GPUtil.getGPUs()

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'available': mem.available,
            'used': mem.used,
            'percent': mem.percent
        }

    def get_gpu_stats(self):
        if not GPU_AVAILABLE or not self.gpu_devices:
            return None

        return [{
            'id': gpu.id,
            'load': gpu.load*100,
            'memory_used': gpu.memoryUsed,
            'memory_total': gpu.memoryTotal,
            'memory_percent': gpu.memoryUtil*100
        } for gpu in self.gpu_devices]

    def display_stats(self, cpu, memory, gpu):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        header = f"\n{' System Monitor ':=^60}\n"
        cpu_str = f"CPU Usage: {cpu}%"
        mem_str = f"Memory: {memory['percent']}% ({memory['used']/1024/1024:.1f}MB/{memory['total']/1024/1024:.1f}MB)"
        
        # Added OS module import
        import os
        
        # Modified display method
        os.system('clear' if os.name == 'posix' else 'cls')
        output = [
            header,
            f"[{timestamp}]",
            f"{cpu_str:<50}",
            f"{mem_str:<50}"
        ]
        if gpu:
            for i, g in enumerate(gpu):
                output.append(f"GPU {i} Load: {g['load']:.1f}%")
                output.append(f"GPU {i} Memory: {g['memory_percent']:.1f}% ({g['memory_used']}MB/{g['memory_total']}MB)")
        print('\n'.join(output))

        if gpu:
            for i, gpu in enumerate(gpu):
                print(f"GPU {i} Load: {gpu['load']:.1f}%")
                print(f"GPU {i} Memory: {gpu['memory_percent']:.1f}% "
                      f"({gpu['memory_used']}MB/{gpu['memory_total']}MB)")

        print("="*60)

if __name__ == "__main__":
    monitor = SystemMonitor()
    try:
        while True:
            cpu = monitor.get_cpu_usage()
            memory = monitor.get_memory_usage()
            gpu = monitor.get_gpu_stats()
            monitor.display_stats(cpu, memory, gpu)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")