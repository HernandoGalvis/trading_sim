"""
close_rules.py
Reglas para cierre de operaciones (placeholder Fase 0).
"""
from trading_sim.domain.models import Operation
from trading_sim.logic.pricing.sl_tp import should_close_sl, should_close_tp

def should_close_operation(operation: Operation, precio_actual: float) -> tuple[bool, str]:
    """
    Determina si una operación debe cerrarse.
    
    Returns:
        tuple: (should_close, reason)
    """
    # Verificar Stop Loss
    if should_close_sl(precio_actual, operation.sl, operation.tipo):
        return True, "STOP_LOSS"
    
    # Verificar Take Profit
    if should_close_tp(precio_actual, operation.tp, operation.tipo):
        return True, "TAKE_PROFIT"
    
    return False, ""

def calculate_pnl(operation: Operation, precio_cierre: float) -> float:
    """Calcula el PnL de una operación."""
    if operation.tipo == "LONG":
        return (precio_cierre - operation.precio_entrada) * operation.cantidad
    else:  # SHORT
        return (operation.precio_entrada - precio_cierre) * operation.cantidad