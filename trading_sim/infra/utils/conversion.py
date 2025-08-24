"""
conversion.py
Utilidades para convertir tipos (migradas desde utils.py original).
"""
import pandas as pd
import numpy as np

def py_native(val):
    if isinstance(val, (np.generic, pd._libs.tslibs.nattype.NaTType)):
        if pd.isna(val):
            return None
        if isinstance(val, np.integer):
            return int(val)
        if isinstance(val, np.floating):
            return float(val)
        if isinstance(val, np.bool_):
            return bool(val)
    if isinstance(val, pd.Timestamp):
        return None if pd.isna(val) else val.to_pydatetime()
    return val

def py_native_dict(d):
    return {k: py_native(v) for k, v in d.items()}