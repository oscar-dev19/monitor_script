# Monitor.py
---
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)



Monitor.py is a Python script designed to monitor system resource utilization, including CPU and memory usage. Optionally, it can also display GPU information if a GPU is available. This script utilizes the `psutil` and `GPUtil` libraries to collect and display system resource data.

## Features

- Monitors CPU usage.
- Monitors memory usage.
- Optionally, monitors GPU usage and GPU memory usage if a GPU is available.

## Prerequisites

Before running the script, make sure you have the required Python libraries installed:

- `psutil`: Used to collect CPU and memory usage information.
- `GPUtil`: Used to check for the presence of GPUs and collect GPU-related information. (Only required if you want to monitor GPUs)

You can install these libraries using pip:

```bash
pip install psutil GPUtil
