"""
run_all.py
Runner principal (placeholder Fase 0).
"""
from ..app.simulator import TradingSimulator
from ..config.settings import settings
from ..infra.logging.logger import logger

def run_simulation():
    """Ejecuta una simulación de ejemplo."""
    logger.info("Iniciando simulación de trading")
    logger.info(f"Configuración: {settings}")
    
    # Crear simulador con capital inicial
    simulator = TradingSimulator(capital_inicial=10000.0)
    
    # Ejemplo básico: abrir una operación
    operation = simulator.opening_service.open_operation(
        id_inversionista=1,
        id_estrategia=1,
        id_senal=1,
        ticker="BTCUSD",
        tipo="LONG",
        precio_entrada=50000.0,
        cantidad=0.1,
        apalancamiento=2
    )
    
    if operation:
        simulator.active_operations.append(operation)
        logger.info(f"Operación abierta: {operation.id_operacion}")
    else:
        logger.warning("No se pudo abrir la operación")
    
    # Simular algunos ticks
    test_prices = [50100, 50200, 49500, 48000]  # Último precio activará SL
    
    for precio in test_prices:
        simulator.process_tick("BTCUSD", precio)
        status = simulator.get_status()
        logger.info(f"Precio: {precio}, Estado: {status}")
    
    logger.info("Simulación completada")
    return simulator.get_status()

if __name__ == "__main__":
    run_simulation()