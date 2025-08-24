"""
capital.py
Adaptado de capital_manager.py actual (simplificado).
Encapsula estado y operaciones sobre capital.
"""
from dataclasses import dataclass

@dataclass
class CapitalState:
    capital_total: float
    capital_bloqueado: float

def required_margin(cantidad: float, precio: float, apalancamiento: int) -> float:
    """Calcula el margen requerido para una operación."""
    if not apalancamiento or apalancamiento <= 0:
        apalancamiento = 1
    return (cantidad * precio) / apalancamiento

def capital_disponible(state: CapitalState) -> float:
    """Retorna el capital disponible para nuevas operaciones."""
    return state.capital_total - state.capital_bloqueado

def can_open_operation(state: CapitalState, cantidad: float, precio: float, apalancamiento: int) -> bool:
    """Verifica si hay suficiente capital para abrir una operación."""
    margin_needed = required_margin(cantidad, precio, apalancamiento)
    return capital_disponible(state) >= margin_needed

def block_capital(state: CapitalState, cantidad: float, precio: float, apalancamiento: int) -> CapitalState:
    """Bloquea capital para una nueva operación."""
    margin_needed = required_margin(cantidad, precio, apalancamiento)
    if not can_open_operation(state, cantidad, precio, apalancamiento):
        raise ValueError("Insufficient capital for operation")
    
    return CapitalState(
        capital_total=state.capital_total,
        capital_bloqueado=state.capital_bloqueado + margin_needed
    )

def release_capital(state: CapitalState, cantidad: float, precio: float, apalancamiento: int, pnl: float) -> CapitalState:
    """Libera capital de una operación cerrada y aplica el PnL."""
    margin_used = required_margin(cantidad, precio, apalancamiento)
    
    return CapitalState(
        capital_total=state.capital_total + pnl,
        capital_bloqueado=max(0, state.capital_bloqueado - margin_used)
    )