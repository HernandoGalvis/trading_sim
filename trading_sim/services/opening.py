"""
opening.py
Servicio de apertura de operaciones (placeholder Fase 0).
"""
from typing import Optional
from datetime import datetime
from ..domain.models import Operation, TipoOperacion
from ..services.capital import CapitalManager
from ..logic.pricing.sl_tp import calculate_sl_tp

class OpeningService:
    """Servicio para abrir operaciones."""
    
    def __init__(self, capital_manager: CapitalManager):
        self.capital_manager = capital_manager
        self._next_id = 1
    
    def open_operation(
        self,
        id_inversionista: int,
        id_estrategia: int,
        id_senal: int,
        ticker: str,
        tipo: TipoOperacion,
        precio_entrada: float,
        cantidad: float,
        apalancamiento: int = 1,
        sl: Optional[float] = None,
        tp: Optional[float] = None
    ) -> Optional[Operation]:
        """Abre una nueva operación."""
        
        # Calcular SL/TP si no se proporcionan
        if sl is None or tp is None:
            calc_sl, calc_tp = calculate_sl_tp(precio_entrada, tipo)
            sl = sl or calc_sl
            tp = tp or calc_tp
        
        # Calcular capital requerido
        capital_requerido = (cantidad * precio_entrada) / apalancamiento
        
        # Verificar disponibilidad de capital
        if not self.capital_manager.can_open_position(capital_requerido):
            return None
        
        # Bloquear capital
        if not self.capital_manager.block_capital(capital_requerido):
            return None
        
        # Crear operación
        operation = Operation(
            id_operacion=self._next_id,
            id_inversionista=id_inversionista,
            id_estrategia=id_estrategia,
            id_senal=id_senal,
            ticker=ticker,
            tipo=tipo,
            ts_apertura=datetime.now(),
            precio_entrada=precio_entrada,
            sl=sl,
            tp=tp,
            cantidad=cantidad,
            apalancamiento=apalancamiento,
            capital_riesgo_usado=capital_requerido,
            valor_total_exposicion=cantidad * precio_entrada,
            precio_max_alcanzado=precio_entrada,
            precio_min_alcanzado=precio_entrada
        )
        
        self._next_id += 1
        return operation