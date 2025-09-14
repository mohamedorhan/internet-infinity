"""
Crypto Engine
=============

Handles encryption and decryption for Internet ∞.
"""

from cryptography.fernet import Fernet


class CryptoEngine:
    def __init__(self, key: bytes = None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message: str) -> bytes:
        return self.cipher.encrypt(message.encode())

    def decrypt(self, token: bytes) -> str:
        return self.cipher.decrypt(token).decode()

    def get_key(self) -> bytes:
        return self.key
