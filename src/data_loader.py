import pandas as pd

def load_metrics(path):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    required = {
        "timestamp","system_id","region","environment","service","cpu_pct",
        "memory_pct","disk_pct","network_latency_ms","error_rate_pct",
        "availability_pct","incident_count"
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df
