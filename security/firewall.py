"""
Unified Firewall
================

Smart firewall for Internet ∞.
"""

from typing import List, Dict, Any


class UnifiedFirewall:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []

    def add_rule(self, rule: Dict[str, Any]) -> None:
        """Add a new firewall rule."""
        self.rules.append(rule)

    def remove_rule(self, rule: Dict[str, Any]) -> None:
        if rule in self.rules:
            self.rules.remove(rule)

    def is_allowed(self, packet: Dict[str, Any]) -> bool:
        """
        Check if a packet passes firewall rules.
        Example rule: {"block_ip": "192.168.0.1"}
        """
        for rule in self.rules:
            if "block_ip" in rule and packet.get("ip") == rule["block_ip"]:
                return False
        return True

    def list_rules(self) -> List[Dict[str, Any]]:
        return self.rules
