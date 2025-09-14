"""
LegacyBridge
============
Bridge between Internet ∞ and the classical legacy Internet (HTTP/HTTPS).
"""

import logging
import requests  # lightweight HTTP client

logger = logging.getLogger(__name__)

class LegacyBridge:
    def __init__(self, firewall=None, persistence=None, crypto=None):
        self.firewall = firewall
        self.persistence = persistence
        self.crypto = crypto
        logger.info("✅ LegacyBridge initialized")

    def send_http(self, url: str, method: str = "GET", data: dict = None):
        """
        Send a simple HTTP request to legacy internet.
        """
        try:
            logger.info(f"🌐 Sending {method} request to {url}")
            if method.upper() == "GET":
                response = requests.get(url, timeout=5)
            elif method.upper() == "POST":
                response = requests.post(url, json=data, timeout=5)
            else:
                logger.warning(f"⚠️ Unsupported method: {method}")
                return None

            logger.info(f"✅ Response [{response.status_code}]: {response.text[:80]}...")
            return response.text
        except Exception as e:
            logger.error(f"❌ LegacyBridge request failed: {e}")
            return None
