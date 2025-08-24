"""
sl_tp.py
Cálculo de SL/TP básicos (placeholder Fase 0).
"""

def calculate_sl_tp(precio_entrada: float, tipo: str, sl_pct: float = 0.02, tp_pct: float = 0.04):
    """Calcula SL/TP básicos basados en porcentajes."""
    if tipo == "LONG":
        sl = precio_entrada * (1 - sl_pct)
        tp = precio_entrada * (1 + tp_pct)
    else:  # SHORT
        sl = precio_entrada * (1 + sl_pct)
        tp = precio_entrada * (1 - tp_pct)
    
    return sl, tp