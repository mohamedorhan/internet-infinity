"""
BioNet: Biological Interface Layer
==================================

The BioNet layer simulates biological signal integration
into Internet ∞. It provides a framework for brainwave,
biometric, and human-signal driven communication.

Key Features:
    - 🧬 Register biological IDs (bio-IDs).
    - 🧠 Capture biological signals (EEG, heart rate, etc.).
    - 🔗 Map bio-signals into network messages.
    - 💾 Persistent state for bio-interfaces.

Scientific Relevance:
    BioNet is inspired by **BCI (Brain-Computer Interfaces)**,
    EEG/ECG signal processing, and next-gen neurotechnology.
    This is a prototype of **bio-networking** in Internet 3.0.

Author: Mohamed Orhan Zeinel
"""

import logging
import random
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class BioNet:
    """
    BioNet: A biological interface simulator for Internet ∞.
    It allows registration of biological IDs and simulates
    signals like brainwaves or vital signs.
    """

    def __init__(self, name: str = "BioNet"):
        self.name = name
        self.bio_ids: Dict[str, str] = {}       # user_id → signal_hash
        self.signals: Dict[str, List[str]] = {} # user_id → list of signals
        logger.info(f"🧬 {self.name} initialized")

    def register_bio_id(self, user_id: str, signal_hash: str) -> bool:
        """Register a biological ID for a user."""
        if user_id not in self.bio_ids:
            self.bio_ids[user_id] = signal_hash
            # Generate synthetic biological signals
            self.signals[user_id] = [
                f"theta:{random.randint(4,7)}Hz",
                f"alpha:{random.randint(8,12)}Hz",
                f"beta:{random.randint(13,30)}Hz",
                f"hr:{random.randint(60,100)}bpm"
            ]
            logger.info(f"🧠 Bio-ID registered: {user_id} → {signal_hash[:8]}...")
            return True
        logger.warning(f"⚠️ Bio-ID already exists: {user_id}")
        return False

    def get_biological_signal(self, user_id: str) -> List[str]:
        """Retrieve biological signals for a registered user."""
        if user_id not in self.signals:
            logger.error(f"❌ No signals found for user: {user_id}")
            return []
        signal_data = self.signals[user_id]
        logger.info(f"📡 BioNet signals for {user_id}: {signal_data}")
        return signal_data

    def map_signal_to_network(self, user_id: str, signal_type: str) -> Dict[str, Any]:
        """Map a biological signal into a simulated network packet."""
        signals = self.get_biological_signal(user_id)
        selected = [s for s in signals if s.startswith(signal_type)]
        if not selected:
            logger.warning(f"⚠️ Signal type {signal_type} not found for {user_id}")
            return {"status": "error", "reason": "signal not found"}

        packet = {
            "user_id": user_id,
            "signal": selected[0],
            "mapped_to": f"packet::{signal_type}::{user_id}",
        }
        logger.info(f"🔗 Signal mapped to network: {packet}")
        return packet

    def show_state(self) -> Dict[str, Any]:
        """Return the current state of registered users and signals."""
        return {
            "bio_ids": list(self.bio_ids.keys()),
            "signals": {uid: sigs for uid, sigs in self.signals.items()},
        }
