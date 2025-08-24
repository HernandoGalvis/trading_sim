"""
base.py
Validador base (placeholder Fase 0).
"""

class BaseValidator:
    """Clase base para validadores."""
    
    def validate(self, *args, **kwargs) -> tuple[bool, str]:
        """
        Valida una condición.
        
        Returns:
            tuple: (is_valid, error_message)
        """
        raise NotImplementedError("Subclasses must implement validate method")

class ValidationResult:
    """Resultado de validación."""
    
    def __init__(self, is_valid: bool, message: str = ""):
        self.is_valid = is_valid
        self.message = message
    
    def __bool__(self):
        return self.is_valid