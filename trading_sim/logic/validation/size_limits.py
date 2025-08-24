"""
size_limits.py
Validador de límites de tamaño (placeholder Fase 0).
"""
from .base import BaseValidator

class SizeLimitsValidator(BaseValidator):
    """Valida límites de tamaño de operaciones."""
    
    def __init__(self, min_size: float = 0.001, max_size: float = 1000000):
        self.min_size = min_size
        self.max_size = max_size
    
    def validate(self, operation_data: dict) -> tuple[bool, str]:
        """Valida que el tamaño esté dentro de los límites."""
        cantidad = operation_data.get('cantidad', 0)
        
        if cantidad < self.min_size:
            return False, f"Cantidad {cantidad} menor al mínimo {self.min_size}"
        
        if cantidad > self.max_size:
            return False, f"Cantidad {cantidad} mayor al máximo {self.max_size}"
        
        return True, ""