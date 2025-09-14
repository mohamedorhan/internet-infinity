#!/usr/bin/env python3
"""
Demo Launcher for Internet ∞ Infinity
-------------------------------------
Runs a lightweight showcase of the system.
"""

from internet_infinity import InternetInfinity


def run_demo():
    print("🎬 Starting Internet ∞ Demo...")
    system = InternetInfinity(mode="demo")
    system.load_layers()

    print("\n=== DEMO SUMMARY ===")
    print(f"✅ Layers initialized: {system.layers}")
    print(f"🔑 Session ID: {system.session_id}")
    print(f"💻 Mode: {system.mode}")
    print("=====================\n")
    print("🚀 Demo completed successfully.")


if __name__ == "__main__":
    run_demo()
