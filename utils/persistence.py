"""
Persistence Utility
===================

Handles saving and loading system state for Internet ∞.
"""

import json
import os
from typing import Any, Dict


class StatePersistence:
    def __init__(self, base_dir: str = "state"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def save(self, filename: str, data: Dict[str, Any]) -> None:
        path = os.path.join(self.base_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"💾 Saved state: {filename}")

    def load(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.base_dir, filename)
        if not os.path.exists(path):
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_all(self) -> None:
        """Placeholder: save all components if needed."""
        pass

    def load_all(self) -> None:
        """Placeholder: load all components if needed."""
        pass
