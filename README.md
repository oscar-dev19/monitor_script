# Monitor.py
---
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)



Monitor.py is a Python script designed to monitor system resource utilization, including CPU and memory usage. Optionally, it can also display GPU information if a GPU is available. This script utilizes the `psutil` and `GPUtil` libraries to collect and display system resource data.

## Features

- Monitors CPU usage.
- Monitors memory usage.
- Optionally, monitors GPU usage and GPU memory usage if a GPU is available.

## Prerequisites

- Python 3.6 or higher
- Required packages specified in [requirements.txt](requirements.txt)

## Installation

1. Clone the repository or download the script
2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Basic execution:
```bash
python3 monitor.py
```

Optional arguments:
- `--interval`: Refresh interval in seconds (default: 1)
- `--gpu`: Enable GPU monitoring (requires compatible hardware)

Example with custom settings:
```bash
python3 monitor.py --interval 2 --gpu
```

Press `Ctrl+C` to exit the monitoring process.

## Monitoring Features

- Monitors CPU usage
- Monitors memory usage
- Optionally monitors GPU usage and GPU memory usage if availablebash
pip install psutil GPUtil
