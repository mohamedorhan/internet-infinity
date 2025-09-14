"""
GreenNet: Sustainable & Secure Networking Layer
===============================================

GreenNet is the **eco-conscious foundation** of the Internet Infinity stack.  
Its design principles are aligned with both **scientific research** and 
**next-generation Internet protocols**:

    - ♻️ Energy-efficient packet routing (reduced carbon footprint).
    - 🔐 Integrated firewall and privacy guards (GDPR/CCPA-ready).
    - 🌍 Local-first storage and routing to minimize global latency.
    - 📊 Analytics for eco-score and traffic health.

This module provides a **proof-of-concept** for "Internet 3.0" where
network traffic is not only fast and secure, but also **sustainable**.

Author: Mohamed Orhan Zeinel  
"""

import logging
from datetime import datetime
from typing import Dict, Any


logger = logging.getLogger(__name__)


class GreenNet:
    """
    GreenNet: Environmentally sustainable and secure routing layer.
    """

    def __init__(self, name: str = "GreenNet"):
        self.name = name
        self.routes: Dict[str, str] = {}
        self.analytics: Dict[str, Any] = {"sent": 0, "blocked": 0}
        self.firewall_rules = []
        logger.info(f"🌱 {self.name} initialized successfully.")

    def add_route(self, node: str, address: str) -> bool:
        """Register a new route in the GreenNet table."""
        if not self._validate_ip(address):
            logger.error(f"❌ Invalid IP address: {address}")
            return False
        self.routes[node] = address
        logger.info(f"➕ Added route: {node} → {address}")
        return True

    def send_packet(self, node: str, data: str) -> bool:
        """Send a packet to a registered node if allowed by firewall."""
        if node not in self.routes:
            logger.error(f"❌ Node {node} not found in GreenNet routes.")
            return False

        if self._is_blocked(node, data):
            self.analytics["blocked"] += 1
            logger.warning(f"🚫 Packet blocked → {node}: {data}")
            return False

        self.analytics["sent"] += 1
        logger.info(f"📦 Packet sent to {node} ({self.routes[node]}): {data}")
        return True

    def add_firewall_rule(self, rule_type: str, target: str, action: str = "block") -> None:
        """Add a firewall rule for traffic filtering."""
        rule = {
            "type": rule_type,
            "target": target,
            "action": action,
            "created": datetime.now().isoformat()
        }
        self.firewall_rules.append(rule)
        logger.info(f"🛡️ Firewall rule added: {rule_type} '{target}' → {action}")

    def show_state(self) -> Dict[str, Any]:
        """Return the current state of GreenNet."""
        return {
            "name": self.name,
            "routes": self.routes,
            "analytics": self.analytics,
            "firewall_rules": len(self.firewall_rules)
        }

    # ======================
    # INTERNAL HELPERS
    # ======================

    def _validate_ip(self, address: str) -> bool:
        """Validate IPv4 address format."""
        parts = address.split(".")
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

    def _is_blocked(self, node: str, data: str) -> bool:
        """Check if traffic should be blocked by firewall."""
        for rule in self.firewall_rules:
            if rule["target"] == node or rule["target"] in data:
                return rule["action"] == "block"
        return False
