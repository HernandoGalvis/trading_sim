"""
size_limits.py
Validador de límites de tamaño (placeholder Fase 0).
"""
from trading_sim.logic.validation.base import BaseValidator, ValidationResult

class SizeLimitsValidator(BaseValidator):
    """Valida límites de tamaño de operación."""
    
    def __init__(self, min_size: float = 0.001, max_size: float = 1000000):
        self.min_size = min_size
        self.max_size = max_size
    
    def validate(self, cantidad: float) -> ValidationResult:
        """Valida que la cantidad esté dentro de los límites."""
        if cantidad < self.min_size:
            return ValidationResult(False, f"Cantidad {cantidad} menor al mínimo {self.min_size}")
        
        if cantidad > self.max_size:
            return ValidationResult(False, f"Cantidad {cantidad} mayor al máximo {self.max_size}")
        
        return ValidationResult(True, "Tamaño válido")

# Instancia global para usar en testing
default_size_validator = SizeLimitsValidator()