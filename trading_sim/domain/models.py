"""
models.py
Modelos simples (dataclasses) para operaciones y capital.
Más adelante se pueden extender o convertir a pydantic.
"""
from dataclasses import dataclass
from typing import Optional, Literal
from datetime import datetime

TipoOperacion = Literal["LONG", "SHORT"]

@dataclass
class Operation:
    id_operacion: Optional[int]
    id_inversionista: int
    id_estrategia: int
    id_senal: int
    ticker: str
    tipo: TipoOperacion
    ts_apertura: datetime
    precio_entrada: float
    sl: float
    tp: float
    cantidad: float
    apalancamiento: int
    capital_riesgo_usado: float
    valor_total_exposicion: float
    precio_max_alcanzado: float
    precio_min_alcanzado: float
    liq_parcial_sl_realizada: bool = False
    id_operacion_padre: Optional[int] = None

@dataclass
class CapitalState:
    capital_total: float
    capital_bloqueado: float