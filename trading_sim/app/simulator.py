"""
simulator.py
Simulador principal (placeholder Fase 0).
"""
from trading_sim.services.capital import CapitalState
from trading_sim.infra.logging.logger import logger

class TradingSimulator:
    """Simulador principal del trading."""
    
    def __init__(self, capital_inicial: float = 10000.0):
        self.capital_state = CapitalState(
            capital_total=capital_inicial,
            capital_bloqueado=0.0
        )
        self.operations = []
        logger.info(f"Simulador iniciado con capital: {capital_inicial}")
    
    def get_capital_info(self) -> dict:
        """Retorna información del capital actual."""
        return {
            "capital_total": self.capital_state.capital_total,
            "capital_bloqueado": self.capital_state.capital_bloqueado,
            "capital_disponible": self.capital_state.capital_total - self.capital_state.capital_bloqueado
        }
    
    def run_simulation(self):
        """Ejecuta la simulación (placeholder)."""
        logger.info("Iniciando simulación...")
        logger.info(f"Estado inicial: {self.get_capital_info()}")
        # Placeholder: aquí iría la lógica de simulación real
        logger.info("Simulación completada (placeholder)")
        
        return self.get_capital_info()