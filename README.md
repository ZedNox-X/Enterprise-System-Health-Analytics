# Enterprise System Health Analytics

A production-style Jupyter Notebook project for analyzing enterprise infrastructure telemetry, detecting operational anomalies, calculating system health scores, and producing an executive risk summary.

## Highlights

- Reproducible synthetic infrastructure dataset (10,000 system observations)
- Data-quality validation and missing-value handling
- CPU, memory, disk, latency, error-rate and availability analysis
- Robust anomaly flagging using standardized metrics
- Composite 0–100 health score
- LOW / MEDIUM / HIGH / CRITICAL risk classification
- Reusable Python modules instead of putting all logic in the notebook
- Unit test for scoring logic
- GitHub-ready structure

- <img width="1536" height="1024" alt="Enterprise System Health Analytics Dashboard" src="https://github.com/user-attachments/assets/e6c74f36-55f1-4e90-b29f-1b3f036f5901" />


## Quick start

```bash
git clone <your-repository-url>
cd enterprise-system-health-analytics

python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r requirements.txt
jupyter lab
```

Open `notebooks/enterprise_system_health_analysis.ipynb`.

## Project structure

```text
notebooks/   Main analysis notebook
data/        Raw and processed telemetry
src/         Reusable Python modules
tests/       Automated tests
reports/     Generated figures/reports
```

## Dataset

The included dataset is synthetic and contains operational telemetry fields such as CPU utilization, memory utilization, disk utilization, network latency, application error rate, availability and incident count. It is intended for portfolio, learning and demonstration purposes.

## Health score

The notebook calculates a composite score from 0 to 100 using resource utilization, network latency and application error rate. The thresholds are demonstration rules rather than an industry standard.

## Testing

```bash
pytest
```

## Suggested GitHub description

> Enterprise Jupyter Notebook for infrastructure telemetry analysis, anomaly detection, health scoring, and operational risk reporting using Python, Pandas, NumPy, and reusable analytics modules.

Updated on 21-09-2026 by Melbin George
