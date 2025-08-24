"""
sl_tp.py
Cálculo de Stop Loss y Take Profit (placeholder Fase 0).
"""

def calculate_sl_price(precio_entrada: float, tipo: str, sl_percent: float) -> float:
    """Calcula el precio de Stop Loss basado en porcentaje."""
    if tipo == "LONG":
        return precio_entrada * (1 - sl_percent / 100)
    else:  # SHORT
        return precio_entrada * (1 + sl_percent / 100)

def calculate_tp_price(precio_entrada: float, tipo: str, tp_percent: float) -> float:
    """Calcula el precio de Take Profit basado en porcentaje."""
    if tipo == "LONG":
        return precio_entrada * (1 + tp_percent / 100)
    else:  # SHORT
        return precio_entrada * (1 - tp_percent / 100)

def should_close_sl(precio_actual: float, sl_price: float, tipo: str) -> bool:
    """Determina si se debe cerrar por Stop Loss."""
    if tipo == "LONG":
        return precio_actual <= sl_price
    else:  # SHORT
        return precio_actual >= sl_price

def should_close_tp(precio_actual: float, tp_price: float, tipo: str) -> bool:
    """Determina si se debe cerrar por Take Profit."""
    if tipo == "LONG":
        return precio_actual >= tp_price
    else:  # SHORT
        return precio_actual <= tp_price