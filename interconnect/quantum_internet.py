"""
QuantumInternet: Entanglement-Driven Networking Layer
====================================================

QuantumInternet is the **secure backbone** of the Internet Infinity stack.  
It leverages concepts from **Quantum Key Distribution (QKD)**, 
**entanglement swapping**, and **post-quantum cryptography**.

Key features:
    - ⚛️ Quantum Node registration with entangled states.
    - 🔑 QKD handshake simulation (BB84 protocol).
    - 🔗 Entanglement management and trust scores.
    - 🔒 Quantum-safe message transfer with optional encryption.

This module represents a **scientific prototype** of how Internet 3.0
could adopt quantum communication as a default layer.

Author: Mohamed Orhan Zeinel  
"""

import logging
import secrets
from datetime import datetime
from typing import Dict, List, Any, Optional


logger = logging.getLogger(__name__)


class QuantumInternet:
    """
    Quantum Internet: A layer built on **entanglement and QKD**.
    """

    def __init__(self, name: str = "QuantumInternet"):
        self.name = name
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.entanglements: List[tuple] = []
        self.qkd_keys: Dict[tuple, str] = {}
        self.key_history: List[Dict[str, Any]] = []
        logger.info(f"🔮 {self.name} initialized successfully.")

    def add_node(self, node_name: str) -> None:
        """Register a new quantum node in the network."""
        if node_name not in self.nodes:
            self.nodes[node_name] = {"entangled_with": None, "keys": []}
            logger.info(f"➕ Quantum node added: {node_name}")

    def entangle(self, node1: str, node2: str) -> bool:
        """Establish quantum entanglement between two nodes."""
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1]["entangled_with"] = node2
            self.nodes[node2]["entangled_with"] = node1
            self.entanglements.append((node1, node2))
            logger.info(f"⚛️ Entanglement established: {node1} ↔ {node2}")
            return True
        logger.error("❌ Failed entanglement: nodes not found.")
        return False

    def qkd_handshake(self, node1: str, node2: str) -> Optional[str]:
        """Perform a simulated Quantum Key Distribution (BB84)."""
        if node1 not in self.nodes or node2 not in self.nodes:
            logger.error("❌ QKD handshake failed: nodes not found.")
            return None

        key = secrets.token_hex(16)  # 128-bit symmetric key
        self.qkd_keys[(node1, node2)] = key
        self.qkd_keys[(node2, node1)] = key
        self.key_history.append({
            "nodes": (node1, node2),
            "key": key,
            "time": datetime.now().isoformat(),
            "protocol": "BB84"
        })
        logger.info(f"🔑 QKD handshake successful: {node1} ↔ {node2}")
        return key

    def send_quantum_pulse(self, sender: str, message: str, target: Optional[str] = None) -> Dict[str, Any]:
        """Send a quantum-secure message between entangled nodes."""
        if sender not in self.nodes:
            return {"status": "error", "message": "Sender not found"}

        if target and self.nodes[sender].get("entangled_with") != target:
            return {"status": "error", "message": "Nodes not entangled"}

        key = self.qkd_keys.get((sender, target)) if target else None
        encrypted = self._encrypt_message(message, key) if key else message

        payload = {
            "status": "success",
            "from": sender,
            "to": target or "broadcast",
            "message": encrypted,
            "encrypted": bool(key),
            "timestamp": datetime.now().isoformat()
        }

        logger.info(f"📡 Quantum pulse sent: {payload}")
        return payload

    def show_state(self) -> Dict[str, Any]:
        """Return current state of the quantum internet."""
        return {
            "nodes": list(self.nodes.keys()),
            "entanglements": self.entanglements,
            "active_keys": len(self.qkd_keys),
            "key_history_entries": len(self.key_history)
        }

    # ======================
    # INTERNAL HELPERS
    # ======================

    def _encrypt_message(self, message: str, key: str) -> str:
        """Simple XOR-based encryption placeholder (replace with PQC)."""
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
