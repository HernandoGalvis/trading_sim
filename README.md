# trading_sim

Skeleton inicial (Fase 0) del simulador de trading modular.

## Objetivo Fase 0
Tener una base limpia que:
- Abra y cierre operaciones (SL/TP) con el capital manager.
- Organice carpetas para crecer sin un script gigante.
- Permita migrar el código viejo copiando funciones (no reescribir).

## Estructura

```
trading_sim/
  app/
    run_all.py
    simulator.py
  config/
    settings.py
    feature_flags.py
  domain/
    models.py
    events.py
  infra/
    logging/
      logger.py
    utils/
      conversion.py
  logic/
    pricing/
      sl_tp.py
    validation/
      base.py
      size_limits.py
    closing/
      close_rules.py
  services/
    capital.py
    opening.py
tests/
  unit/
    test_size_limits.py
```

## Próximos pasos
1. Verificar que `pytest` corre (1 test dummy).
2. Migrar lógica real (capital_manager / operaciones) en Fase 1.
3. Comparar capital final vs versión antigua (subset).
4. Tag: `fase0_skeleton_ok`.

## Instalación rápida
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Requisitos próximos (Fase 1)
- Migrar validador tamaño/capital (size_limits real).
- Extraer apertura real.
- Pipeline de validadores.

## Notas
Repo público: documentar cambios breves aquí hasta introducir CHANGELOG.