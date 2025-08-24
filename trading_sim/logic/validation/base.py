"""
base.py
Validador base (placeholder Fase 0).
"""

class BaseValidator:
    """Clase base para todos los validadores."""
    
    def validate(self, operation_data: dict) -> tuple[bool, str]:
        """Retorna (es_valido, mensaje_error)."""
        return True, ""