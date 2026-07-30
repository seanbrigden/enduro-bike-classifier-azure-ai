# logger.py
# Placeholder logging module for API and inference events

import logging

# Basic logger configuration (placeholder)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("enduro-bike-classifier")

def log_event(message: str):
    """
    Placeholder logging function.
    Will be expanded to include structured logs, metadata, and Azure Monitor integration.
    """
    logger.info(f"[placeholder] {message}")
