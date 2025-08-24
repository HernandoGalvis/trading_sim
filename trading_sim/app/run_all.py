"""
run_all.py
Runner principal del simulador (placeholder Fase 0).
"""
from trading_sim.app.simulator import TradingSimulator
from trading_sim.config.settings import settings
from trading_sim.infra.logging.logger import logger

def main():
    """Punto de entrada principal."""
    logger.info("Iniciando trading_sim...")
    logger.info(f"Configuración: {settings}")
    
    # Crear simulador
    simulator = TradingSimulator(capital_inicial=10000.0)
    
    # Ejecutar simulación
    resultado = simulator.run_simulation()
    
    logger.info(f"Resultado final: {resultado}")
    return resultado

if __name__ == "__main__":
    main()