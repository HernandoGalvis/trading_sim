"""
test_size_limits.py
Test dummy para validar que pytest funciona (Fase 0).
"""
import pytest
from trading_sim.logic.validation.size_limits import SizeLimitsValidator

def test_size_limits_validator_valid():
    """Test que verifica validación exitosa."""
    validator = SizeLimitsValidator(min_size=0.001, max_size=1000)
    result = validator.validate(10.0)
    
    assert result.is_valid is True
    assert "válido" in result.message.lower()

def test_size_limits_validator_too_small():
    """Test que verifica rechazo por tamaño muy pequeño."""
    validator = SizeLimitsValidator(min_size=0.001, max_size=1000)
    result = validator.validate(0.0001)
    
    assert result.is_valid is False
    assert "menor" in result.message.lower()

def test_size_limits_validator_too_large():
    """Test que verifica rechazo por tamaño muy grande."""
    validator = SizeLimitsValidator(min_size=0.001, max_size=1000)
    result = validator.validate(10000)
    
    assert result.is_valid is False
    assert "mayor" in result.message.lower()

def test_dummy_always_pass():
    """Test dummy que siempre pasa para verificar que pytest funciona."""
    assert True