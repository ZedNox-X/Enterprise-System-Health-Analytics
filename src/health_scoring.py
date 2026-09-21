import numpy as np

def calculate_health_score(df):
    result = df.copy()
    cpu_penalty = np.clip((result["cpu_pct"] - 60) * 0.55, 0, 25)
    mem_penalty = np.clip((result["memory_pct"] - 65) * 0.45, 0, 20)
    disk_penalty = np.clip((result["disk_pct"] - 70) * 0.50, 0, 20)
    latency_penalty = np.clip((result["network_latency_ms"] - 80) * 0.08, 0, 20)
    error_penalty = np.clip(result["error_rate_pct"] * 2.2, 0, 25)
    result["health_score"] = (
        100 - cpu_penalty - mem_penalty - disk_penalty -
        latency_penalty - error_penalty
    ).clip(0, 100).round(2)
    result["risk_level"] = np.select(
        [result["health_score"] < 50, result["health_score"] < 70, result["health_score"] < 85],
        ["CRITICAL", "HIGH", "MEDIUM"], default="LOW"
    )
    return result
