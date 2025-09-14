"""
Auth Manager
============

Handles user authentication for Internet ∞.
"""

import hashlib
from typing import Dict


class AuthManager:
    def __init__(self):
        # Default users (username: password_hash)
        self.users: Dict[str, str] = {
            "admin": self._hash("admin123"),
            "guest": self._hash("guest"),
        }

    def _hash(self, password: str) -> str:
        """Hash passwords for storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username: str, password: str) -> bool:
        """Verify username & password."""
        if username not in self.users:
            return False
        return self.users[username] == self._hash(password)

    def add_user(self, username: str, password: str) -> None:
        self.users[username] = self._hash(password)

    def remove_user(self, username: str) -> None:
        if username in self.users:
            del self.users[username]
