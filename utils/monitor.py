"""
System Monitor
==============

Monitors CPU, RAM, and uptime for Internet ∞.
"""

import psutil
import time
from typing import Dict, Any


class SystemMonitor:
    def __init__(self):
        self.start_time = time.time()

    def get_metrics(self) -> Dict[str, Any]:
        return {
            "uptime": time.time() - self.start_time,
            "cpu_percent": psutil.cpu_percent(interval=0.5),
            "ram_percent": psutil.virtual_memory().percent,
            "ram_used_mb": round(psutil.virtual_memory().used / 1024 / 1024, 2),
        }
