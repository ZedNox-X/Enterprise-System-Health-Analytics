import pandas as pd

def clean_metrics(df):
    result = df.copy()
    numeric = result.select_dtypes(include="number").columns
    for col in numeric:
        result[col] = result[col].fillna(result[col].median())
    # Robust clipping for obvious sensor/network outliers.
    for col in ["cpu_pct","memory_pct","disk_pct","error_rate_pct","availability_pct"]:
        if col in result:
            result[col] = result[col].clip(lower=0)
    result["network_latency_ms"] = result["network_latency_ms"].clip(lower=0, upper=1000)
    return result

def validate_ranges(df):
    checks = {
        "cpu_pct": (0, 100),
        "memory_pct": (0, 100),
        "disk_pct": (0, 100),
        "error_rate_pct": (0, 100),
        "availability_pct": (0, 100),
        "network_latency_ms": (0, float("inf")),
    }
    return {c: bool(df[c].between(lo, hi).all()) for c, (lo, hi) in checks.items()}
