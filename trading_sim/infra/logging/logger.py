"""
logger.py
Logger central. Reusar en todos los módulos.
"""
import logging
import os

LOG_LEVEL = os.getenv("SIM_LOG_LEVEL", "INFO").upper()

logger = logging.getLogger("trading_sim")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(LOG_LEVEL)