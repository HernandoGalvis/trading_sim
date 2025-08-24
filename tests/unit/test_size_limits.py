"""
test_size_limits.py
Test dummy para verificar que pytest funciona (Fase 0).
"""
import pytest
from trading_sim.logic.validation.size_limits import SizeLimitsValidator

def test_size_limits_validator():
    """Test dummy para validador de límites de tamaño."""
    validator = SizeLimitsValidator(min_size=0.001, max_size=1000)
    
    # Caso válido
    valid_data = {"cantidad": 10.0}
    is_valid, message = validator.validate(valid_data)
    assert is_valid is True
    assert message == ""
    
    # Caso inválido - muy pequeño
    invalid_small = {"cantidad": 0.0001}
    is_valid, message = validator.validate(invalid_small)
    assert is_valid is False
    assert "menor al mínimo" in message
    
    # Caso inválido - muy grande
    invalid_large = {"cantidad": 2000}
    is_valid, message = validator.validate(invalid_large)
    assert is_valid is False
    assert "mayor al máximo" in message

def test_dummy_always_passes():
    """Test dummy que siempre pasa para verificar pytest."""
    assert True