"""
feature_flags.py
Interruptores para activar controles futuros sin tocar la lógica base.
En Fase 0 casi todos quedan en False salvo lo esencial.
"""
class FeatureFlags:
    enable_size_limits = False          # Se activa en Fase 1
    enable_confirmation = False         # Fase 2
    enable_trailing = False             # Fase 3
    enable_partial_liq_sl = False       # Fase 3
    enable_drawdown = False             # Fase 5
    enable_strategy_loss_limit = False  # Fase 5
    enable_ledger = False               # Fase 6
    enable_leverage_range = False       # Fase 7
    enable_risk_to_sl_sizing = False    # Fase 7
    enable_commissions = False          # Fase 8
    enable_slippage = False             # Fase 8

flags = FeatureFlags()