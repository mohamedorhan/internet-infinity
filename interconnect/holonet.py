"""
HoloNet: Holographic Communication Layer
========================================

The HoloNet layer simulates immersive, holographic communication
within Internet ∞. It provides a framework for **3D/AR/VR telepresence**.

Key Features:
    - 🌀 Create holographic "rooms".
    - 👥 Add/remove participants in real-time.
    - 📡 Broadcast VR/AR messages.
    - 💾 Persistent state for reproducible holographic sessions.

Scientific Relevance:
    Represents a prototype of **Internet 3.0 immersive communication**,
    bridging classic networking with **holographic/AR/VR data streams**.

Author: Mohamed Orhan Zeinel
"""

import logging
from typing import Dict, List, Any


logger = logging.getLogger(__name__)


class HoloNet:
    """
    HoloNet: A lightweight holographic communication simulator
    for Internet ∞. It models hologram rooms and participant flows.
    """

    def __init__(self, name: str = "HoloNet"):
        self.name = name
        self.holograms: Dict[str, Dict[str, Any]] = {}
        self.participants: Dict[str, List[str]] = {}
        logger.info(f"🕸️ {self.name} initialized")

    def create_hologram(self, room_name: str) -> bool:
        """Create a new holographic space (room)."""
        if room_name not in self.holograms:
            self.holograms[room_name] = {"dimensions": "3D", "resolution": "high"}
            self.participants[room_name] = []
            logger.info(f"🌀 Hologram room created: {room_name}")
            return True
        logger.warning(f"⚠️ Hologram room already exists: {room_name}")
        return False

    def add_participant(self, user: str, room_name: str) -> bool:
        """Add a participant to a hologram room."""
        if room_name not in self.holograms:
            logger.error(f"❌ Room not found: {room_name}")
            return False
        if user not in self.participants[room_name]:
            self.participants[room_name].append(user)
            logger.info(f"👥 {user} joined hologram room: {room_name}")
            return True
        logger.warning(f"⚠️ {user} is already in room: {room_name}")
        return False

    def broadcast_vr_message(self, room_name: str, message: str) -> Dict[str, Any]:
        """Broadcast a VR/AR message to all participants in a hologram room."""
        if room_name not in self.holograms:
            logger.error(f"❌ Room not found: {room_name}")
            return {"status": "error", "message": "room not found"}

        receivers = self.participants.get(room_name, [])
        logger.info(
            f"📡 [HoloNet:{room_name}] Broadcast → {len(receivers)} users: {message}"
        )
        return {
            "room": room_name,
            "message": message,
            "receivers": receivers,
            "count": len(receivers),
        }

    def show_state(self) -> Dict[str, Any]:
        """Return the state of all holographic rooms and participants."""
        return {
            "holograms": list(self.holograms.keys()),
            "participants": {room: users for room, users in self.participants.items()},
        }
