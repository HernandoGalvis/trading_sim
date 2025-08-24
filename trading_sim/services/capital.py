"""
capital.py
Adaptado de capital_manager.py actual.
Encapsula estado y operaciones sobre capital.
"""
from dataclasses import dataclass

@dataclass
class CapitalState:
    capital_total: float
    capital_bloqueado: float

def required_margin(cantidad: float, precio: float, apalancamiento: int) -> float:
    if not apalancamiento or apalancamiento <= 0:
        apalancamiento = 1
    return (cantidad * precio) / apalancamiento

def calculate_capital_risk(cantidad: float, precio_entrada: float, sl: float, tipo: str) -> float:
    """Calcula el capital en riesgo basado en SL."""
    if tipo == "LONG":
        return cantidad * abs(precio_entrada - sl)
    else:  # SHORT
        return cantidad * abs(sl - precio_entrada)

class CapitalManager:
    def __init__(self, capital_inicial: float):
        self.state = CapitalState(
            capital_total=capital_inicial,
            capital_bloqueado=0.0
        )
    
    def can_open_position(self, capital_requerido: float) -> bool:
        """Verifica si hay capital disponible."""
        available = self.state.capital_total - self.state.capital_bloqueado
        return available >= capital_requerido
    
    def block_capital(self, amount: float) -> bool:
        """Bloquea capital para una operación."""
        if self.can_open_position(amount):
            self.state.capital_bloqueado += amount
            return True
        return False
    
    def release_capital(self, amount: float):
        """Libera capital al cerrar una operación."""
        self.state.capital_bloqueado = max(0, self.state.capital_bloqueado - amount)
    
    def apply_pnl(self, pnl: float):
        """Aplica ganancia/pérdida al capital total."""
        self.state.capital_total += pnl