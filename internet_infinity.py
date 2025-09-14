#!/usr/bin/env python3
"""
Internet ∞ Infinity
--------------------
Main CLI entrypoint for the Next-Generation Internet project.
"""

import logging
import importlib
import pkgutil
from pathlib import Path

# Setup logger
logging.basicConfig(
    filename="logs/infinity.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger("InternetInfinity")


class InternetInfinity:
    def __init__(self, mode="simulation"):
        self.mode = mode
        self.layers = []
        self.session_id = "20250914_000000"

        logger.info("🚀 Initializing Internet ∞ Ultimate System...")

    def load_layers(self):
        """Dynamically load all layers from interconnect/"""
        package = "interconnect"
        package_path = Path(__file__).parent / "interconnect"

        logger.info("🔍 Scanning interconnect/ for dynamic layers...")

        for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
            try:
                module = importlib.import_module(f"{package}.{module_name}")
                cls_name = "".join([part.capitalize() for part in module_name.split("_")])
                layer_class = getattr(module, cls_name)
                instance = layer_class()
                self.layers.append(cls_name)
                logger.info(f"✅ Loaded layer: {cls_name}")
            except Exception as e:
                logger.error(f"❌ Failed to load module {module_name}.py: {e}")

        logger.info(f"🌐 System initialized with {len(self.layers)} layers.")
        logger.info(f"🔑 Session ID: {self.session_id}")
        logger.info(f"💻 Mode: {self.mode}")

    def start_cli(self):
        """Start a simple text CLI."""
        print("\n=== 🌐 Internet ∞ ULTIMATE CLI ===")
        print(f"Session ID: {self.session_id}")
        print(f"Mode: {self.mode}")
        print(f"Layers: {self.layers}\n")
        print("🔒 You are NOT logged in. Login required for full access.")

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "1234":
            print("✅ Login successful! Full access granted.")
        else:
            print("❌ Login failed. Running in restricted mode.")


if __name__ == "__main__":
    system = InternetInfinity(mode="simulation")
    system.load_layers()
    system.start_cli()
