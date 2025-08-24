"""
opening.py
Servicio para apertura de operaciones (placeholder Fase 0).
"""
from trading_sim.domain.models import Operation, TipoOperacion
from trading_sim.services.capital import CapitalState, block_capital
from datetime import datetime

def create_operation(
    id_inversionista: int,
    id_estrategia: int,
    id_senal: int,
    ticker: str,
    tipo: TipoOperacion,
    precio_entrada: float,
    sl: float,
    tp: float,
    cantidad: float,
    apalancamiento: int,
    capital_state: CapitalState
) -> tuple[Operation, CapitalState]:
    """Crea una operación y actualiza el estado del capital."""
    
    # Calcular valores derivados
    valor_total_exposicion = cantidad * precio_entrada
    capital_riesgo_usado = valor_total_exposicion / apalancamiento
    
    # Crear operación
    operation = Operation(
        id_operacion=None,  # Se asignará cuando se guarde en BD
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
        capital_riesgo_usado=capital_riesgo_usado,
        valor_total_exposicion=valor_total_exposicion,
        precio_max_alcanzado=precio_entrada,
        precio_min_alcanzado=precio_entrada,
        liq_parcial_sl_realizada=False,
        id_operacion_padre=None
    )
    
    # Actualizar capital
    new_capital_state = block_capital(capital_state, cantidad, precio_entrada, apalancamiento)
    
    return operation, new_capital_state