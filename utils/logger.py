"""
Logger Utility
==============

Configures global logging for Internet ∞.
"""

import logging
import sys


def setup_logger(name: str = "InternetInfinity") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


# Initialize a default global logger
logger = setup_logger()
