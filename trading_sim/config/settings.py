"""
settings.py
Configuración base (Fase 0). Se puede sustituir luego por .env o BD.
"""
from dataclasses import dataclass
import os

@dataclass
class SimSettings:
    fecha_inicio: str = os.getenv("SIM_FECHA_INICIO", "2025-01-01 00:00:00")
    fecha_fin: str = os.getenv("SIM_FECHA_FIN", "2025-01-01 00:00:00")
    max_workers: int = int(os.getenv("SIM_MAX_WORKERS", "4"))

settings = SimSettings()