"""
Validator Utility
=================

Performs input validation and basic checks.
"""

from typing import Any


class Validator:
    @staticmethod
    def is_valid_username(username: str) -> bool:
        return username.isalnum() and 3 <= len(username) <= 20

    @staticmethod
    def is_valid_password(password: str) -> bool:
        return len(password) >= 6

    @staticmethod
    def validate_not_empty(value: Any) -> bool:
        return value is not None and value != ""
