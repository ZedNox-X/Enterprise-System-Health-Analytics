import pandas as pd
from src.health_scoring import calculate_health_score

def test_health_score_is_bounded():
    df = pd.DataFrame({
        "cpu_pct":[50], "memory_pct":[50], "disk_pct":[50],
        "network_latency_ms":[30], "error_rate_pct":[0]
    })
    result = calculate_health_score(df)
    assert 0 <= result.loc[0, "health_score"] <= 100
    assert result.loc[0, "risk_level"] == "LOW"
