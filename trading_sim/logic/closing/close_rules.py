"""
close_rules.py
Reglas de cierre básicas SL/TP (Fase 0).
"""

def should_close_sl(precio_actual: float, sl: float, tipo: str) -> bool:
    """Determina si se debe cerrar por SL."""
    if tipo == "LONG":
        return precio_actual <= sl
    else:  # SHORT
        return precio_actual >= sl

def should_close_tp(precio_actual: float, tp: float, tipo: str) -> bool:
    """Determina si se debe cerrar por TP."""
    if tipo == "LONG":
        return precio_actual >= tp
    else:  # SHORT
        return precio_actual <= tp

def calculate_pnl(precio_entrada: float, precio_salida: float, cantidad: float, tipo: str) -> float:
    """Calcula PnL de una operación."""
    if tipo == "LONG":
        return cantidad * (precio_salida - precio_entrada)
    else:  # SHORT
        return cantidad * (precio_entrada - precio_salida)