"""
events.py
Eventos básicos (placeholder) para un futuro ledger.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Event:
    ts: datetime
    tipo: str
    detalle: str

@dataclass
class OpenEvent(Event):
    id_operacion: int
    capital_riesgo: float

@dataclass
class CloseEvent(Event):
    id_operacion: int
    pnl: float