"""
NeuralNet: Adaptive Intelligence Layer
======================================

The NeuralNet layer is responsible for **learning**, **pattern recognition**, 
and **adaptive decision-making** across Internet ∞.

Key Features:
    - 🧠 Learn communication patterns.
    - 🔮 Predict user/system behavior.
    - 📊 Maintain weighted confidence scores.
    - 💾 Persistent state for reproducible research.

Scientific Relevance:
    Inspired by machine learning models, this component 
    demonstrates how a **self-optimizing network brain** could evolve.

Author: Mohamed Orhan Zeinel
"""

import logging
import random
from typing import Dict, Any, List


logger = logging.getLogger(__name__)


class NeuralNet:
    """
    NeuralNet: A lightweight adaptive intelligence simulator
    for Internet ∞. It learns patterns and predicts outcomes.
    """

    def __init__(self, name: str = "NeuralNet"):
        self.name = name
        self.patterns: List[str] = []
        self.weights: Dict[str, float] = {}
        logger.info(f"🧠 {self.name} initialized")

    def learn_pattern(self, pattern: str) -> bool:
        """Learn a new communication or user pattern."""
        if pattern not in self.patterns:
            self.patterns.append(pattern)
            self.weights[pattern] = random.uniform(0.5, 1.0)
            logger.info(f"🧩 Learned new pattern: {pattern}")
            return True
        logger.warning(f"⚠️ Pattern already known: {pattern}")
        return False

    def predict(self, input_pattern: str) -> str:
        """Predict the best matching pattern given input."""
        matches = [p for p in self.patterns if input_pattern in p]
        if not matches:
            logger.warning(f"❓ Unknown input pattern: {input_pattern}")
            return "Unknown pattern"

        best = max(matches, key=lambda x: self.weights.get(x, 0))
        prediction = f"Prediction: {best} (confidence={self.weights[best]:.2f})"
        logger.info(f"🔮 {prediction}")
        return prediction

    def reinforce(self, pattern: str, success: bool) -> None:
        """Reinforce (reward or penalize) learned patterns."""
        if pattern in self.weights:
            delta = 0.05 if success else -0.05
            self.weights[pattern] = max(0.0, min(1.0, self.weights[pattern] + delta))
            logger.info(
                f"🔧 Reinforced pattern: {pattern} → {self.weights[pattern]:.2f}"
            )

    def show_state(self) -> Dict[str, Any]:
        """Return current learned patterns and weights."""
        return {
            "patterns": self.patterns,
            "weights": self.weights,
            "total_learned": len(self.patterns),
        }
