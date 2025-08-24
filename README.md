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
1. Verificar que `pytest` corre (aunque sea 1 test dummy).
2. Copiar la lógica real de capital_manager.py y operaciones.py al lugar indicado.
3. Ejecutar un "mini run" (luego añadiremos un script temporal) para comparar resultados con la versión anterior.
4. Etiquetar (tag) `fase0_skeleton_ok`.

## Instalación rápida

```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
pytest
```

## Requisitos próximos (Fase 1)
- Migrar validador tamaño/capital (size_limits).
- Extraer apertura real.
- Preparar pipeline de validadores.

## Notas
Este repo es privado: documenta cambios breves en el README hasta introducir CHANGELOG.