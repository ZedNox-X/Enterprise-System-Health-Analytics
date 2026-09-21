import pandas as pd

def add_anomaly_flags(df):
    result = df.copy()
    result["latency_z"] = (result["network_latency_ms"] - result["network_latency_ms"].mean()) / result["network_latency_ms"].std(ddof=0)
    result["error_z"] = (result["error_rate_pct"] - result["error_rate_pct"].mean()) / result["error_rate_pct"].std(ddof=0)
    result["anomaly_flag"] = (result["latency_z"].abs() >= 3) | (result["error_z"].abs() >= 3)
    return result
