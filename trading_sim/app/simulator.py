"""
simulator.py
Simulador mínimo (placeholder Fase 0).
"""
from typing import List
from ..domain.models import Operation
from ..services.capital import CapitalManager
from ..services.opening import OpeningService
from ..logic.closing.close_rules import should_close_sl, should_close_tp, calculate_pnl
from ..infra.logging.logger import logger

class TradingSimulator:
    """Simulador principal de trading."""
    
    def __init__(self, capital_inicial: float):
        self.capital_manager = CapitalManager(capital_inicial)
        self.opening_service = OpeningService(self.capital_manager)
        self.active_operations: List[Operation] = []
        self.closed_operations: List[Operation] = []
    
    def process_tick(self, ticker: str, precio: float):
        """Procesa un tick de precio."""
        operations_to_close = []
        
        for op in self.active_operations:
            if op.ticker != ticker:
                continue
            
            # Actualizar precios máximos y mínimos
            op.precio_max_alcanzado = max(op.precio_max_alcanzado, precio)
            op.precio_min_alcanzado = min(op.precio_min_alcanzado, precio)
            
            # Verificar cierre por SL o TP
            if should_close_sl(precio, op.sl, op.tipo):
                operations_to_close.append((op, precio, "SL"))
            elif should_close_tp(precio, op.tp, op.tipo):
                operations_to_close.append((op, precio, "TP"))
        
        # Cerrar operaciones
        for op, precio_cierre, motivo in operations_to_close:
            self._close_operation(op, precio_cierre, motivo)
    
    def _close_operation(self, operation: Operation, precio_cierre: float, motivo: str):
        """Cierra una operación."""
        pnl = calculate_pnl(operation.precio_entrada, precio_cierre, operation.cantidad, operation.tipo)
        
        # Aplicar PnL al capital
        self.capital_manager.apply_pnl(pnl)
        
        # Liberar capital bloqueado
        self.capital_manager.release_capital(operation.capital_riesgo_usado)
        
        # Mover a operaciones cerradas
        self.active_operations.remove(operation)
        self.closed_operations.append(operation)
        
        logger.info(f"Operación {operation.id_operacion} cerrada por {motivo}. PnL: {pnl:.2f}")
    
    def get_status(self) -> dict:
        """Retorna el estado actual del simulador."""
        return {
            "capital_total": self.capital_manager.state.capital_total,
            "capital_bloqueado": self.capital_manager.state.capital_bloqueado,
            "operaciones_activas": len(self.active_operations),
            "operaciones_cerradas": len(self.closed_operations)
        }