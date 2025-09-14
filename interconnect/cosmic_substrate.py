"""
CosmicSubstrate: Interstellar Communication Layer
=================================================

The CosmicSubstrate is a **speculative layer** for Internet 3.0+.  
It is based on **resonance fields**, **trust propagation**, and 
**interconnected cosmic channels**.

Key Features:
    - ✨ Node registration with trust scores.
    - 📡 Channel creation (resonance-based multicast).
    - 🌈 Resonance establishment between nodes.
    - 🔒 Trust-aware secure pulse messaging.

Scientific Relevance:
    This layer demonstrates how **non-local connectivity** 
    (inspired by physics + cosmology) could be simulated 
    in a networking context.

Author: Mohamed Orhan Zeinel  
"""

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional


logger = logging.getLogger(__name__)


class CosmicSubstrate:
    """
    CosmicSubstrate: A communication medium based on resonance fields.
    """

    def __init__(self, name: str = "CosmicSubstrate"):
        self.name = name
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.channels: Dict[str, Dict[str, Any]] = {}
        self.trust_scores: Dict[str, Dict[str, int]] = {}
        self.channel_logs: Dict[str, List[Dict[str, Any]]] = {}
        logger.info(f"🌌 {self.name} initialized successfully.")

    def add_node(self, node_name: str) -> None:
        """Register a node in the cosmic substrate."""
        if node_name not in self.nodes:
            self.nodes[node_name] = {"channels": [], "trust": 50}
            self.trust_scores[node_name] = {}
            logger.info(f"✨ Node registered: {node_name}")

    def create_channel(self, channel_name: str) -> None:
        """Create a cosmic resonance channel."""
        if channel_name not in self.channels:
            self.channels[channel_name] = {"nodes": [], "encrypted": False}
            self.channel_logs[channel_name] = []
            logger.info(f"📡 Channel created: {channel_name}")

    def join_channel(self, node_name: str, channel_name: str) -> bool:
        """Add a node to a resonance channel."""
        if node_name not in self.nodes or channel_name not in self.channels:
            logger.error("❌ Node or channel not found.")
            return False

        if channel_name not in self.nodes[node_name]["channels"]:
            self.nodes[node_name]["channels"].append(channel_name)
        if node_name not in self.channels[channel_name]["nodes"]:
            self.channels[channel_name]["nodes"].append(node_name)

        logger.info(f"🔗 Node {node_name} joined channel {channel_name}")
        return True

    def establish_resonance(self, node1: str, node2: str) -> bool:
        """Establish resonance between two nodes (high trust link)."""
        if node1 not in self.nodes or node2 not in self.nodes:
            logger.error("❌ Cannot establish resonance: nodes missing.")
            return False

        trust = 85  # Default resonance trust level
        self.trust_scores[node1][node2] = trust
        self.trust_scores[node2][node1] = trust
        logger.info(f"🌈 Resonance established: {node1} ↔ {node2} (Trust={trust})")
        return True

    def send_pulse(
        self,
        sender: str,
        message: str,
        channel: Optional[str] = None,
        target: Optional[str] = None,
        encrypted: bool = False,
    ) -> Dict[str, Any]:
        """Send a cosmic pulse (message)."""
        if sender not in self.nodes:
            return {"status": "error", "message": "Sender not found"}

        # Trust check
        if target and self.trust_scores.get(sender, {}).get(target, 0) < 30:
            logger.warning(f"⚠️ Low trust: {sender} → {target}")
            return {"status": "low_trust"}

        payload = {
            "from": sender,
            "to": target or "broadcast",
            "channel": channel or "direct",
            "message": message,
            "encrypted": encrypted,
            "timestamp": datetime.now().isoformat(),
        }

        if channel and channel in self.channel_logs:
            self.channel_logs[channel].append(payload)

        logger.info(f"✨ Cosmic pulse transmitted: {payload}")
        return payload

    def show_state(self) -> Dict[str, Any]:
        """Return the current state of the cosmic substrate."""
        return {
            "nodes": list(self.nodes.keys()),
            "channels": list(self.channels.keys()),
            "trust_scores": self.trust_scores,
            "channel_logs": {k: len(v) for k, v in self.channel_logs.items()},
        }
